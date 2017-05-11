## Conference Calendar

Adds events from selected conference categories to Google calendar

### Setup
- Use [this wizard](https://console.developers.google.com/start/api?id=calendar) to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to credentials.
- On the Add credentials to your project page, click the Cancel button.
- At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
- Select the Credentials tab, click the Create credentials button and select OAuth client ID.
- Select the application type Other, enter the name "Google Calendar API Quickstart", and click the Create button.
- Click OK to dismiss the resulting dialog.
- Click the file_download (Download JSON) button to the right of the client ID.
- Move this file to your working directory and rename it client_secret.json

- Run setup.sh

### Running
Run the program using the following command:
`python fetchConf.py --cat "<category>"`

This will fetch all the events for this category from confsearch.org and create calendar events for their deadlines in your primary calendar.
Only primary calendar is supported at the moment.

Remember to put category in quotes since this will handle the case when there is a space involved in the name of category.

The list of available categories can be fetched using
`python fetchConf.py --list`

#### First time only
The sample will attempt to open a new window or tab in your default browser. If this fails, copy the URL from the console and manually open it in your browser.

If you are not already logged into your Google account, you will be prompted to log in. If you are logged into multiple Google accounts, you will be asked to select one account to use for the authorization.
Click the Accept button.
The sample will proceed automatically, and you may close the window/tab.


use `python fetchConf -h` to get further information
