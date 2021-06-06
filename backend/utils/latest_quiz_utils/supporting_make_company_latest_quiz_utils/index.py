# -------------------------------------------------------------- Imports
import os, time
import datetime
from flask import Flask, session, url_for, send_from_directory, render_template

# ------------------------ Pages START ------------------------
# Index page
from backend.page_templates_backend.index_page_backend.index_page_render_template import index_page_render_template
# Slack authentication pages
from backend.page_templates_backend.slack_confirm_oauth_redirect_dashboard_backend.slack_confirm_oauth_redirect_dashboard_index import slack_confirm_oauth_redirect_dashboard_index
# Slack dashboard pages
from backend.page_templates_backend.dashboard_page_backend.dashboard_index_page_render_template import dashboard_index_page_render_template
# Slack account pages
from backend.page_templates_backend.account_page_backend.account_index_page_render_template import account_index_page_render_template
from backend.utils.slack.send_channel_test_message.send_channel_test_message import send_channel_test_message
from backend.page_templates_backend.account_page_backend.logout import logout
# Create question pages
from backend.page_templates_backend.waitlist_page_backend.waitlist_create_question_page_backend.waitlist_create_question_page_render_template import waitlist_create_question_page_render_template
from backend.page_templates_backend.waitlist_page_backend.waitlist_create_question_page_backend.waitlist_create_question_add_to_database_processing import waitlist_create_question_add_to_database_processing
from backend.page_templates_backend.waitlist_page_backend.waitlist_create_question_page_backend.waitlist_create_question_confirm_on_waitlist_page_render_template import waitlist_create_question_confirm_on_waitlist_page_render_template
from backend.page_templates_backend.create_question_page_backend.create_question_index_page_render_template import create_question_index_page_render_template
from backend.page_templates_backend.create_question_page_backend.create_question_submission_page_backend.create_question_submission_processing import create_question_submission_processing
from backend.page_templates_backend.create_question_page_backend.create_question_submission_page_backend.create_question_submission_success_page_render_template import create_question_submission_success_page_render_template
# Quiz Settings pages
from backend.page_templates_backend.quiz_settings_page_backend.quiz_settings_index_page_render_template import quiz_settings_index_page_render_template
from backend.page_templates_backend.quiz_settings_page_backend.edit_quiz_settings_page_backend.edit_quiz_settings_index_page_render_template import edit_quiz_settings_index_page_render_template
from backend.page_templates_backend.quiz_settings_page_backend.edit_quiz_settings_page_backend.edit_quiz_settings_submit_new_quiz_settings import edit_quiz_settings_submit_new_quiz_settings
# Quiz Feedback pages
from backend.page_templates_backend.quiz_feedback_page_backend.quiz_feedback_index_page_render_template import quiz_feedback_index_page_render_template
from backend.page_templates_backend.quiz_feedback_page_backend.quiz_feedback_submission_page_backend.quiz_feedback_processing import quiz_feedback_processing
from backend.page_templates_backend.quiz_feedback_page_backend.quiz_feedback_submission_page_backend.quiz_feedback_success_page_render_template import quiz_feedback_success_page_render_template
# ------------------------ Pages END ------------------------


# ------------------------ App setup START ------------------------
# Set the timezone of the application when user creates account is will be in US/Easterm time
os.environ['TZ'] = 'US/Eastern'
time.tzset()
# Flask constructor
app = Flask(__name__)
#app = Flask(__name__, static_folder="static", template_folder="templates")

# To use a session, there has to be a secret key. The string should be something difficult to guess
app.secret_key = os.urandom(64)
# Set session variables to perm so that user can remain signed in for x days
app.permanent_session_lifetime = datetime.timedelta(days=30)

# For removing cache from images for quiz questions. The URL was auto caching and not updating
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

  # ------------------------ Handleing Error Messages START ------------------------
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
  return render_template("error_404_page_templates/index.html")
  # ------------------------ Handleing Error Messages END ------------------------
# ------------------------ App setup END ------------------------


# ------------------------ Pages - Register START ------------------------
# Index page
app.register_blueprint(index_page_render_template, url_prefix="")
# Slack authentication pages
app.register_blueprint(slack_confirm_oauth_redirect_dashboard_index, url_prefix="")
# Slack dashboard pages
app.register_blueprint(dashboard_index_page_render_template, url_prefix="")
# Slack account pages
app.register_blueprint(account_index_page_render_template, url_prefix="")
app.register_blueprint(send_channel_test_message, url_prefix="")
app.register_blueprint(logout, url_prefix="")
# Create question pages
app.register_blueprint(waitlist_create_question_page_render_template, url_prefix="")
app.register_blueprint(waitlist_create_question_add_to_database_processing, url_prefix="")
app.register_blueprint(waitlist_create_question_confirm_on_waitlist_page_render_template, url_prefix="")
app.register_blueprint(create_question_index_page_render_template, url_prefix="")
app.register_blueprint(create_question_submission_processing, url_prefix="")
app.register_blueprint(create_question_submission_success_page_render_template, url_prefix="")
# Quiz Settings pages
app.register_blueprint(quiz_settings_index_page_render_template, url_prefix="")
app.register_blueprint(edit_quiz_settings_index_page_render_template, url_prefix="")
app.register_blueprint(edit_quiz_settings_submit_new_quiz_settings, url_prefix="")
# Quiz Feedback pages
app.register_blueprint(quiz_feedback_index_page_render_template, url_prefix="")
app.register_blueprint(quiz_feedback_processing, url_prefix="")
app.register_blueprint(quiz_feedback_success_page_render_template, url_prefix="")
# ------------------------ Pages - Register END ------------------------





# =========================================================================================================== Run app
# Run the main program
if __name__ == "__main__":

  # Check environment variable that was passed in from user on the command line
  server_env = os.environ.get('TESTING', 'false')
  # ------------------------ Running on localhost START ------------------------
  if server_env and server_env == 'true':
    print('RUNNING ON LOCALHOST')
    app.run(debug = True)#, use_reloader=False)
  # ------------------------ Running on localhost END ------------------------


  # ------------------------ Running on heroku server START ------------------------
  else:
    # port and run for Heroku
    print('RUNNING ON PRODUCTION')
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)
  # ------------------------ Running on heroku server END ------------------------