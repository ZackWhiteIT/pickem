# Pickem

## A Wordpress managed sports pick 'em game, focused on college football

Pickem is a toolkit I created out of neccessity for my college football pick 'em group. I've used a manual workflow for a few years and found ways to automate this process with incremental improvements.

## Environment Setup (Not Included)
- A Wordpress web server with admin access
- Jetpack with Contact Forms enabled
- Some process to take the pick results and generate standings (Google Sheets, Excel, SQL, etc.)

## Setting up the Pickem CLI
- Clone the repo
- Download ESPN's [college football schedule](http://www.espn.com/college-football/schedule) for the week manually

## Generating the Schedule CSV
```
python schedule_scraper.py your_schedule.html > schedule.csv
```

Where your_schedule.html is the the html file you downloaded from ESPN.

## Generating the Wordpress Contact Form Code
```
python generate_wp_contact_form.py schedule.csv
```

This will print out the contact form within the terminal. Simply copy/paste this into a new post in Wordpress.

## Filtering by rank & team

By default, the contact form generator only adds Top 25 and SEC teams to the CSV file. To change this functionality, simply change the values of RANKED_FILTER and TEAM_FILTER.

## Extending Functionality

In theory, you could use the same code base for other leagues and sports as long as the HTML table structure is the same as ESPN's college football schedule web page. Alternatively, you could create a CSV schedule manually or with other software and use the contact form generator to create the Wordpress short code.

## Future Improvements
- Automate HTML schedule download (currently blocked by ESPN)
- Automate posting contact form as a new Wordpress post
- Add Contact Form 7 compatibility & use Contact Form DB to store/retrieve picks
- Integrate standings, users, and results from Google Docs or do away with the Docs dependency altogether

## FAQ

### Why not use ESPN/Yahoo!/CBS as your pick 'em engine?

Customization and full control. My group did not want to pick teams they didn't follow, so we chose the SEC and Top 25. We also aren't fans of confidence points or picking against the spread.

### Why doesn't this toolkit do [insert feature here]?

It's probably crossed my mind, but I haven't gotten around to it.

### Is there a working example of this toolkit & pick 'em setup?

Yes, my group is managed at my [website](http://pickem.zackwhiteit.com/).

## License

This software is licensed under The MIT License (MIT). See the [LICENSE](LICENSE) file in the top distribution directory for the full license text.
