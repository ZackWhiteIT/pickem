import os
import sys
import csv

"""
CSV Import Format:
HOME_TEAM_RANK,HOME_TEAM,AWAY_TEAM_RANK,AWAY_TEAM
#1,Princeton,#2,Yale

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

if(len(sys.argv) == 2):
    RANKED_FILTER = True
    TEAM_FILTER = ['Alabama', 'Auburn', 'LSU', 'Arkansas', 'Texas A&M',
                   'Missouri', 'Tennessee', 'Vanderbilt', 'Georgia', 'Florida',
                   'South Carolina', 'Kentucky', 'Ole Miss', 'Mississippi State']
    IMPORT_PATH = sys.argv[1]
    import_file = open(os.path.abspath(IMPORT_PATH), 'r')

    #Generate contact form header code
    wp_contact_form_code = "[contact-form]\n[contact-field label='Name' type='name' required='1'/]\n[contact-field label='Email' type='email' required='1'/]"

    #Open CSV file for editing
    csvreader = csv.reader(import_file, delimiter=',')

    for row in csvreader:
        #CSV Field Mapping
        home_team_rank = str(row[0])
        home_team = str(row[1])
        away_team_rank = str(row[2])
        away_team = str(row[3])

        #Create label
        if away_team_rank and home_team_rank:
            label = "{} {} @ {} {}".format(away_team_rank,away_team,home_team_rank,home_team)
        elif away_team_rank:
            label = "{} {} @ {}".format(away_team_rank,away_team,home_team)
        elif home_team_rank:
            label = "{} @ {} {}".format(away_team,home_team_rank,home_team)
        else:
            label = "{} @ {}".format(away_team,home_team)

        #Generate contact form radio button code
        if RANKED_FILTER:
            if home_team_rank or away_team_rank:
                wp_contact_form_code += "\n[contact-field label='{}' type='radio' required='1' options='{},{}'/]".format(label,away_team,home_team)
            elif home_team in TEAM_FILTER or away_team in TEAM_FILTER:
                wp_contact_form_code += "\n[contact-field label='{}' type='radio' required='1' options='{},{}'/]".format(label,away_team,home_team)
            else:
                pass
        else:
            if home_team in TEAM_FILTER or away_team in TEAM_FILTER:
                wp_contact_form_code += "\n[contact-field label='{}' type='radio' required='1' options='{},{}'/]".format(label,away_team,home_team)

    #Close contact form code
    wp_contact_form_code += "\n[/contact-form]"
    print(wp_contact_form_code)
    import_file.close()

else:
    print('Error: Invalid and/or missing argument(s)\nArguments: ' + str(sys.argv))
