import sqlite3
import re
import yaml
import os

# --------------------------------------
# sql init
# --------------------------------------
con = sqlite3.connect('RequirementTypes.db')
cur = con.cursor()

con2 = sqlite3.connect('DebugGameplay.sqlite')
cur2 = con2.cursor()
# --------------------------------------
# sql init
# --------------------------------------
quoted = re.compile('\".+\"')

def process_args(args, template, name=None):

	args = list(args)

	for i in range(len(args)):

		argName = name[i] if name else ""
		argType = template[i]
		arg = args[i]

		if arg == None:
			args[i] = "NULL"
		elif argType == "TEXT" and not arg.isdigit():
			if quoted.match(arg):
				pass
			else:
				args[i] = "\"%s\"" % arg
		else:
			args[i] = str(arg)

	return args

# --------------------------------------
# retrieve table into
# --------------------------------------
cur2.execute("SELECT name, dflt_value, type FROM pragma_table_info('Requirements') c;")
table_info = cur2.fetchall()

requirements_names		= [i[0] for i in table_info]
requirements_types		= [i[2] for i in table_info]
requirements_defaults	= process_args([i[1] for i in table_info], requirements_types)

cur2.execute("SELECT name, dflt_value, type FROM pragma_table_info('RequirementArguments') c;")
table_info = cur2.fetchall()

requirementArgs_names		= [i[0] for i in table_info]
requirementArgs_types		= [i[2] for i in table_info]
requirementArgs_defaults	= process_args([i[1] for i in table_info], requirementArgs_types)
# --------------------------------------
#  Cache list of requirements from outside the main database
# --------------------------------------
cachedRequirementTypes = cur.execute("SELECT DISTINCT RequirementID FROM Requirements").fetchall()
cachedRequirementTypes = [i[0] for i in cachedRequirementTypes]
# --------------------------------------
# --------------------------------------
cur.execute("SELECT DISTINCT RequirementType FROM RequirementsList")
requirementTypes = cur.fetchall()

for row in requirementTypes:

	requirementType = row[0]
	cur.execute("SELECT RequirementID, Name FROM RequirementsList WHERE RequirementType = ? ORDER BY Name DESC", (requirementType,))
	argumentNames = cur.fetchall();

	untested = not bool(argumentNames[0][0])
	hasArguments = bool(argumentNames[0][1])

	filename = 'Output/RequirementType.' + requirementType + '.md'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w', encoding='utf-8') as object_file:
		# -----------------------------
		#  Frontmatter
		# -----------------------------
		file_yaml = {}
		file_yaml["title"] = requirementType

		file_yaml["tags"] = []
		file_yaml["tags"].append("RequirementType")

		object_file.write('---\n')
		yaml.dump(file_yaml, object_file)
		object_file.write('---\n')
		# -----------------------------
		#  Title and Intro
		# -----------------------------
		# object_file.write('# ' + requirementType + "\n")
		object_file.write('This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types\n')

		if untested:
			object_file.write('\n> [!warning] Warning \n>\n')
			object_file.write('> This RequirementType exists in the database but is never used! Proceed with caution!\n')

		# -----------------------------
		#  Arguments
		# -----------------------------
		object_file.write('\n## Info\n')
		object_file.write('> [!info] '+requirementType+'\n>\n')

		chimpInfo = cur.execute("SELECT CLASS, ARGUMENTS, `VALUES`, DATATYPE, DESCRIPTION FROM ChimpRequirements WHERE INPUT = ?", (requirementType,)).fetchall()
		chimpArgInfo = {}
		for row in chimpInfo:
			if row[1]:
				chimpArgInfo[row[1]] = (row[2], row[3], row[4])

		requirementClass = chimpInfo[0][0] if chimpInfo and bool(chimpInfo[0][0]) else "Unknown"
		object_file.write('> * Class: `%s`\n' % requirementClass)
		object_file.write('> * Arguments:\n')

		if (untested):
			object_file.write('>\t* *Unknown*\n')
		elif (not hasArguments):
			object_file.write('>\t* **This RequirementType has no Arguments**\n')
		else:
			for argument in argumentNames:
				argName = argument[1]
				if argName:
					argType = "Unknown"
					argNote = None
					argValues = None

					try:
						argType = chimpArgInfo[argName][1]
						argNote = chimpArgInfo[argName][2]
						argValues = chimpArgInfo[argName][0]
					except:
						pass

					object_file.write('>\t* %s `%s`\n' % (argName, argType))
					if argNote:
						object_file.write('>\t\t* %s\n' % argNote.replace("\\n", "\r>\t\t  "))
					if argValues:
						argValues = argValues.replace("\r\n", "\r>\t\t  ")
						argValues = argValues.replace("\\n", "\r>\t\t  ")
						object_file.write('>\t\t* %s\n' % argValues)
		# -----------------------------
		#  Samples
		# -----------------------------
		cur.execute("""
			SELECT DISTINCT RequirementID FROM RequirementsList
			WHERE RequirementType = ?""",
			(requirementType,)
		)
		samples = cur.fetchall();

		if len(samples) > 0 and samples[0][0]:
			object_file.write('\n## Samples\n')

			for sample in samples:

				requirementID = sample[0]
				targetCur = cur if requirementID in cachedRequirementTypes else cur2
				# -----------------------------
				#  Requirements
				# -----------------------------
				# Get columns whcih are different from the default values
				reqCols = []
				sampleRequirement = targetCur.execute("SELECT * FROM Requirements WHERE RequirementID = ?", (requirementID,)).fetchone()
				sampleRequirement = process_args(sampleRequirement, requirements_types)

				for i in range(len(sampleRequirement)):
					if sampleRequirement[i] != requirements_defaults[i]:
						reqCols.append(i)

				columnNames	= [requirements_names[i] for i in reqCols]
				values		= [sampleRequirement[i] for i in reqCols]

				object_file.write('\n```SQL {title="%s"}\n'%requirementID)

				object_file.write(
					"INSERT INTO Requirements\n\t(\n\t\t%s\n\t)\nVALUES\n\t"
					%
					",\n\t\t".join(columnNames)
				)

				object_file.write(
					"(\n\t\t%s\n\t);\n\n"
					%
					",\n\t\t".join(values)
				)
				# -----------------------------
				#  RequirementArguments
				# -----------------------------
				reqArgCols	= {}
				sampleArgs	= targetCur.execute("SELECT * FROM RequirementArguments WHERE RequirementID = ?", (requirementID,)).fetchall()

				if len(sampleArgs) > 0:

					for i in sampleArgs:
						k = process_args(i, requirementArgs_types)
						for j in range(len(i)):
							if k[j] != requirementArgs_defaults[j]:
								reqArgCols[j] = j

					reqArgNames = [requirementArgs_names[i] for i in reqArgCols]
					object_file.write(
						"INSERT INTO RequirementArguments\n\n\t(\n\t\t%s\n\t)\nVALUES\n\t"
						%
						",\n\t\t".join(reqArgNames)
					)

					for i in range(len(sampleArgs)):

						arg = sampleArgs[i]
						arg = process_args(arg, requirementArgs_types, requirementArgs_names)
						comma = "," if i < len(sampleArgs)-1 else ";"

						object_file.write(
							"(\n\t\t%s\n\t)%s\n\t"
							%
							(",\n\t\t".join([arg[i] for i in reqArgCols]), comma)
						)
				# -----------------------------
				# -----------------------------
				object_file.write('```\n')