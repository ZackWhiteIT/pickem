import os
import sys
import csv

"""
CSV Import Format:
GAME_NAME,DATE,HOME_TEAM_RANK,HOME_TEAM,AWAY_TEAM_RANK,AWAY_TEAM
National Championship,1/1/1900,1,Princeton,2,Yale

The GAME_NAME column is required but can be left blank to generate a HOME_TEAM vs. AWAY_TEAM description.

Example Wordpress Contact Form Code:
[contact-form]
[contact-field label='Name' type='name' required='1'/]
[contact-field label='Email' type='email' required='1'/]
[contact-field label='New Orleans Bowl 12/20/2014' type='radio' required='1' options=' Louisiana Lafayette, Nevada'/]
[/contact-form]

This generates the following look in Wordpress:
National Championship - #1 Princeton vs. #2 Yale - 1/1/1900
Options:
- Princeton
- Yale
"""

if(len(sys.argv) == 3):
	IMPORT_PATH = sys.argv[1]
	EXPORT_PATH = sys.argv[2]
	
	import_file = open(os.path.abspath(IMPORT_PATH), 'r')
	
	#if(os.path.exists(os.path.abspath(EXPORT_PATH)) == False):
		#print('Oops.')
		#os.mkdir(os.path.dirname(os.path.abspath(EXPORT_PATH)))
		
	export_file = open(os.path.abspath(EXPORT_PATH), 'w')
	
	#Generate contact form header code
	wp_contact_form_code = "[contact-form]\n[contact-field label='Name' type='name' required='1'/]\n[contact-field label='Email' type='email' required='1'/]"
	
	#Open CSV file for editing
	csvreader = csv.reader(import_file, delimiter=',')
	
	#Skip header row
	next(csvreader)
	
	for row in csvreader:
		#CSV Field Mapping
		game_name = str(row[0])
		game_date = str(row[1])
		home_team_rank = str(row[2])
		home_team = str(row[3])
		away_team_rank = str(row[4])
		away_team = str(row[5])
		
		#Formatting
		if(len(home_team_rank) > 0):
			home_team_rank = '#' + home_team_rank + ' '
		if(len(away_team_rank) > 0):
			away_team_rank = '#' + away_team_rank + ' '
		if(len(game_name) > 0):
			game_name += ' - '
		
		#Create label
		game_name = game_name + away_team_rank + away_team + ' @ ' + home_team_rank + home_team + ' - ' + game_date
		
		#Generate contact form radio button code
		wp_contact_form_code += "\n[contact-field label='" + game_name + "' type='radio' required='1' options='" + away_team + ", " + home_team + "'/]"
	
	#Close contact form code
	wp_contact_form_code += "\n[/contact-form]"
	
	export_file.write(wp_contact_form_code)
	
	export_file.close()
	import_file.close()
 
else:
	print('Error: Invalid and/or missing argument(s)\nArguments: ' + str(sys.argv))