import sqlite3
import yaml
import os

con = sqlite3.connect('Events.db')
cur = con.cursor()

cur.execute("SELECT * FROM ScrapedEvents")

rows = cur.fetchall()

for row in rows:
	eventType = row[1]
	eventName = row[0]
	eventLongName =	eventType + '.' + eventName

	hasEvents = row[3]

	filename = 'Output/' + eventLongName + '.md'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w', encoding='utf-8') as object_file:
		# -----------------------------
		#  Frontmatter
		# -----------------------------
		file_yaml = {}
		file_yaml["title"] = eventLongName

		file_yaml["tags"] = []
		file_yaml["tags"].append("Events/"+eventType)

		object_file.write('---\n')
		yaml.dump(file_yaml, object_file)
		object_file.write('---\n')
		# -----------------------------
		#  Title and Intro
		# -----------------------------
		object_file.write('# ' + eventLongName + "\n")
		object_file.write('This is an [Event](civ-6/lua/Events.md). Please refer to that page for more information on Events\n')
		exists = cur.execute(
			'SELECT :eventName IN (SELECT Event FROM EventsFiraxis UNION SELECT Event FROM GameEventsFiraxis);',
			{"eventName": eventName}
		).fetchone()[0]

		if not exists:
			object_file.write('> [!warning] Warning \n>\n')
			object_file.write('> This Event has been scraped from the game\'s binaries, but has not been used by Firaxis in the game\'s various scripts. Use with caution!\n')
		# -----------------------------
		#  Usage
		# -----------------------------
		exampleTable = "Events" if hasEvents else "GameEvents"
		arguments = cur.execute(
			'SELECT PARAMETER, TYPE FROM ChimpEventsTable WHERE EVENT=? AND PARAMETER!="" ORDER BY "ORDER" ASC;',
			(eventName,)
		).fetchall()

		argumentTable = []
		for argument in arguments:
			argumentTable.append('*'+argument[0]+'*')

		object_file.write('\n## Usage\n')
		object_file.write('> [!example] Example\n>\n')
		object_file.write('> **'+exampleTable+'.'+eventName+'**( ')
		object_file.write(', '.join(argumentTable))
		object_file.write(' )\n')

		for argument in arguments:
			object_file.write('* **'+argument[0]+'**')
			if argument[1]!="":
				object_file.write('    '+argument[1])
			object_file.write('\n')
		# -----------------------------
		#  Usage, Part 2
		# -----------------------------
		existString = ""
		if row[2] and row[3]:
			existString = ' exists in GameEvents. It also exists in Events.\n'
		elif row[2] and not row[3]:
			existString = ' exists in GameEvents. It doesn\'t exist in Events.\n'
		elif not row[2] and row[3]:
			existString = ' doesn\'t exist in GameEvents. It DOES exist in Events.\n'
		elif not row[2] and not row[3]:
			existString = ' is imaginary and you should forget about it.\n'
		object_file.write('\n'+eventName+existString)

		existsEvents = cur.execute(
			'SELECT :eventName IN (SELECT Event FROM EventsFiraxis);',
			{"eventName": eventName}
		).fetchone()[0]

		existsGameEvents = cur.execute(
			'SELECT :eventName IN (SELECT Event FROM GameEventsFiraxis);',
			{"eventName": eventName}
		).fetchone()[0]

		firaxisString = ""
		if existsGameEvents and existsEvents:
			firaxisString = 'Firaxis has used %s with GameEvents AND Events.'
		elif existsGameEvents and not existsEvents:
			firaxisString = 'Firaxis has used %s with only GameEvents.'
		elif not existsGameEvents and existsEvents:
			firaxisString = 'Firaxis has used %s with only Events.'
		elif not existsGameEvents and not existsEvents:
			firaxisString = 'Firaxis has never used %s in its Lua scripts.'
		object_file.write('**'+(firaxisString % eventName)+'**\n')

con.close()