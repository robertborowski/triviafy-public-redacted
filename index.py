# Imports
from flask import Flask, session, url_for, send_from_directory
import os, time
import datetime
from backend.all_pages.landing_page_backend.landing_page_render import landing_page_render
#from backend.all_pages.create_account_page_backend.create_account_page_render import create_account_page_render
#from backend.all_pages.create_account_page_backend.create_account_to_postgres import create_account_to_postgres
#from backend.slack.connecting_to_slack.connect_to_slack_workspace_channel import connect_to_slack_workspace_channel
from backend.all_pages.slack_confirm_page.slack_confirm_page_render import slack_confirm_page_render

# App setup
# Set the timezone of the application when user creates account is will be in US/Easterm time
os.environ['TZ'] = 'US/Eastern'
time.tzset()
# Flask constructor
app = Flask(__name__)
# To use a session, there has to be a secret key. The string should be something difficult to guess
app.secret_key = os.urandom(64)
# Set session variables to perm so that user can remain signed in
app.permanent_session_lifetime = datetime.timedelta(days=365)

# App.register's
app.register_blueprint(landing_page_render, url_prefix="")
#app.register_blueprint(create_account_page_render, url_prefix="")
#app.register_blueprint(create_account_to_postgres, url_prefix="")
#app.register_blueprint(connect_to_slack_workspace_channel, url_prefix="")
app.register_blueprint(slack_confirm_page_render, url_prefix="")



# Run the main program
if __name__ == "__main__":

  server_env = os.environ.get('TESTING', 'false')

  # if localhost
  if server_env and server_env == 'true':
    print('RUNNING ON LOCALHOST')
    app.run(debug = False)
  else:
    # port and run for Heroku
    print('RUNNING ON PRODUCTION')
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)