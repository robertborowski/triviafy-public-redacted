# -------------------------------------------------------------- Imports: all supporting backend files/packages
import os, time
import datetime
from flask import Flask, session, url_for, send_from_directory
from backend.page_templates_backend.index_page_backend.index_page_render_template import index_page_render_template
from backend.page_templates_backend.slack_confirm_oauth_redirect_dashboard_backend.slack_confirm_oauth_redirect_dashboard_index import slack_confirm_oauth_redirect_dashboard_index
from backend.page_templates_backend.dashboard_page_backend.dashboard_index_page_render_template import dashboard_index_page_render_template

from backend.page_templates_backend.dashboard_page_backend.dashboard_send_channel_test_message import dashboard_send_channel_test_message
from backend.page_templates_backend.account_settings_page_backend.logout import logout



# -------------------------------------------------------------- App setup: timezone, register app
# Set the timezone of the application when user creates account is will be in US/Easterm time
os.environ['TZ'] = 'US/Eastern'
time.tzset()

# Flask constructor
app = Flask(__name__)

# To use a session, there has to be a secret key. The string should be something difficult to guess
app.secret_key = os.urandom(64)

# Set session variables to perm so that user can remain signed in for x days
app.permanent_session_lifetime = datetime.timedelta(days=30)

# App.register's
app.register_blueprint(index_page_render_template, url_prefix="")
app.register_blueprint(slack_confirm_oauth_redirect_dashboard_index, url_prefix="")
app.register_blueprint(dashboard_index_page_render_template, url_prefix="")

app.register_blueprint(dashboard_send_channel_test_message, url_prefix="")
app.register_blueprint(logout, url_prefix="")



# =========================================================================================================== Run app
# Run the main program
if __name__ == "__main__":

  # Check environment variable that was passed in from user on the command line
  server_env = os.environ.get('TESTING', 'false')

  # -------------------------------------------------------------- Running on localhost
  if server_env and server_env == 'true':
    print('RUNNING ON LOCALHOST')
    app.run(debug = True)#, use_reloader=False)

  # -------------------------------------------------------------- NOT running on localhost
  else:
    # port and run for Heroku
    print('RUNNING ON PRODUCTION')
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)