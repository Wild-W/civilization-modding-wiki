import sqlite3
import re
import yaml
import os

# --------------------------------------
# sql init
# --------------------------------------
con = sqlite3.connect('EffectTypes.db')
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
cur2.execute("SELECT name, dflt_value, type FROM pragma_table_info('Modifiers') c;")
table_info = cur2.fetchall()

modifiers_names		= [i[0] for i in table_info]
modifiers_types		= [i[2] for i in table_info]
modifiers_defaults	= process_args([i[1] for i in table_info], modifiers_types)

cur2.execute("SELECT name, dflt_value, type FROM pragma_table_info('ModifierArguments') c;")
table_info = cur2.fetchall()

modifierArgs_names		= [i[0] for i in table_info]
modifierArgs_types		= [i[2] for i in table_info]
modifierArgs_defaults	= process_args([i[1] for i in table_info], modifierArgs_types)

# --------------------------------------
# For each EffectType
# --------------------------------------
cur.execute("SELECT DISTINCT EffectType, Untested FROM EffectArguments")
effectTypes = cur.fetchall()

for row in effectTypes:

	effectType = row[0]
	untested = row[1]
	cur.execute("SELECT ArgumentName FROM EffectArguments WHERE EffectType = ?", (effectType,))
	argumentNames = cur.fetchall()

	samples = {}

	for row2 in argumentNames:
		argumentName = row2[0]

		if argumentName:
			cur2.execute("""
				SELECT ModifierId FROM Modifiers
				WHERE ModifierType IN (SELECT ModifierType FROM DynamicModifiers WHERE EffectType = ?)
				AND ModifierId IN (SELECT ModifierId FROM ModifierArguments WHERE Name = ?)
				ORDER BY rowid
				LIMIT 1
			""", (effectType, argumentName))

			try:
				modifierId = cur2.fetchone()[0]
				samples[modifierId] = modifierId
			except:
				pass

	filename = 'Output/EffectType.' + effectType + '.md'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w', encoding='utf-8') as object_file:
		# -----------------------------
		#  Frontmatter
		# -----------------------------
		file_yaml = {}
		file_yaml["title"] = effectType

		file_yaml["tags"] = []
		file_yaml["tags"].append("EffectType")

		object_file.write('---\n')
		yaml.dump(file_yaml, object_file)
		object_file.write('---\n')
		# -----------------------------
		#  Title and Intro
		# -----------------------------
		# object_file.write('# ' + effectType + "\n")
		object_file.write('This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type\n')

		if untested:
			object_file.write('> [!warning] Warning \n>\n')
			object_file.write('> This EffectType exists in the database but is never used! Proceed with caution!\n')
		# -----------------------------
		#  Title and Intro
		# -----------------------------
		object_file.write('\n## Info\n')
		object_file.write('> [!info] '+effectType+'\n>\n')
		chimpInfo = cur.execute("SELECT DISTINCT CLASS FROM ChimpEffects WHERE INPUT = ? LIMIT 1", (effectType,)).fetchone()

		effectClass = chimpInfo[0] if chimpInfo and chimpInfo[0] != '' else "Unknown"
		object_file.write('> * Class: `%s`\n' % effectClass)
		object_file.write('> * Parameters:\n')

		argList = cur.execute("""
			SELECT DISTINCT ArgumentName FROM EffectArguments
			WHERE EffectType = ? AND ArgumentName != "";
		""", (effectType,)).fetchall()

		if argList and len(argList) > 0:
			for arg in argList:

				argName = arg[0]
				argData = cur.execute("""
					SELECT DATATYPE, DESCRIPTION, "VALUES (IF APPLICABLE)" FROM ChimpEffects
					WHERE ARGUMENTS = ?
					AND INPUT = ?
				""", (argName, effectType)).fetchone()

				hasArgType = (argData is not None)
				argType = argData[0] if hasArgType else 'Unknown'
				object_file.write('>\t* %s `%s`\n' % (argName, argType))

				if hasArgType:
					if argData[1] != '':
						object_file.write('>\t\t* %s\n' % argData[1].replace("\\n", "\r>\t\t  "))
					if argData[2] != '':
						object_file.write('>\t\t* %s\n' % argData[2].replace("\\n", "\r>\t\t  "))
		else:
			object_file.write('>  * -\n')
		# -----------------------------
		#  Samples
		# -----------------------------
		if len(samples) > 0:
			object_file.write('\n## Samples\n')
		for sample in samples:

			reqCols = []
			sampleModifier = cur2.execute("SELECT * FROM Modifiers WHERE ModifierId = ?", (sample,)).fetchone()
			sampleModifier = process_args(sampleModifier, modifiers_types)


			for i in range(len(sampleModifier)):
				if sampleModifier[i] != modifiers_defaults[i]:
					reqCols.append(i)
			# -----------------------------
			#  Modifiers
			# -----------------------------
			object_file.write('\n```SQL {title="%s"}\n'%sample)
			reqNames = [modifiers_names[i] for i in reqCols]
			samepleVals = [sampleModifier[i] for i in reqCols]
			object_file.write(
				"INSERT INTO Modifiers\n\t(\n\t\t%s\n\t)\nVALUES\n\t"
				%
				",\n\t\t".join(reqNames)
			)

			object_file.write(
				"(\n\t\t%s\n\t);\n\n"
				%
				",\n\t\t".join(samepleVals)
			)
			# -----------------------------
			#  ModifierArguments
			# -----------------------------
			reqArgCols	= {}
			sampleArgs	= cur2.execute("SELECT * FROM ModifierArguments WHERE ModifierId = ?", (sample,)).fetchall()

			for i in sampleArgs:

				k = process_args(i, modifierArgs_types)

				for j in range(len(i)):
					if k[j] != modifierArgs_defaults[j]:
						reqArgCols[j] = j

			reqArgNames = [modifierArgs_names[i] for i in reqArgCols]
			object_file.write(
				"INSERT INTO ModifierArguments\n\t(\n\t\t%s\n\t)\nVALUES\n\t"
				%
				",\n\t\t".join(reqArgNames)
			)

			for i in range(len(sampleArgs)):

				arg = sampleArgs[i]
				arg = process_args(arg, modifierArgs_types, modifierArgs_names)
				comma = "," if i < len(sampleArgs)-1 else ";"

				object_file.write(
					"(\n\t\t%s\n\t)%s\n\t"
					%
					(",\n\t\t".join([arg[i] for i in reqArgCols]), comma)
				)

			object_file.write('\n```\n\n')