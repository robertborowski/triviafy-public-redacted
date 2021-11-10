# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.uuid_and_timestamp.create_timestamp import create_timestamp_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.utils.free_trial_period_utils.check_if_free_trial_period_is_expired_days_left import check_if_free_trial_period_is_expired_days_left_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
from backend.db.queries.update_queries.update_queries_triviafy_user_login_information_table_slack.update_account_consent_email import update_account_consent_email_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
from backend.utils.cached_login.check_cookie_browser import check_cookie_browser_function
import json
from backend.utils.send_emails.send_email_with_slack_setup_attachment_template import send_email_with_slack_setup_attachment_template_function
from backend.db.queries.insert_queries.insert_queries_triviafy_emails_sent_table.insert_triviafy_emails_sent_table import insert_triviafy_emails_sent_table_function
from backend.utils.check_paid_latest_month_utils.check_if_user_team_channel_combo_paid_latest_month import check_if_user_team_channel_combo_paid_latest_month_function

# -------------------------------------------------------------- App Setup
email_permission_notification_consent_processing = Blueprint("email_permission_notification_consent_processing", __name__, static_folder="static", template_folder="templates")
@email_permission_notification_consent_processing.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@email_permission_notification_consent_processing.route("/notifications/email/permission/processing", methods=['GET','POST'])
def email_permission_notification_consent_processing_function():
  localhost_print_function('=========================================== /notifications/email/permission/processing Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  try:
    # ------------------------ Page Pre Load Check - User Logged In Through Cookies START ------------------------
    # Check if user logged in through cookies
    user_nested_dict = check_if_user_login_through_cookies_function()
    # ------------------------ Page Pre Load Check - User Logged In Through Cookies END ------------------------

    # ------------------------ Page Pre Load Check - Redirect Check - Free Trial / Latest Month Paid START ------------------------
    # Check if user Team/Channel combo paid the latest month
    user_team_channeL_paid_latest_month = check_if_user_team_channel_combo_paid_latest_month_function(user_nested_dict)
    
    # If user's company did not pay latest month
    if user_team_channeL_paid_latest_month == False:
      # Check if user free trial is expired
      user_nested_dict = check_if_free_trial_period_is_expired_days_left_function(user_nested_dict)
      if user_nested_dict == None or user_nested_dict == True:
        return redirect('/subscription', code=302)

      days_left = str(user_nested_dict['trial_period_days_left_int']) + " days left."
      if user_nested_dict['trial_period_days_left_int'] == 1:
        days_left = str(user_nested_dict['trial_period_days_left_int']) + " day left."

      free_trial_ends_info = "Free Trial Ends: " + user_nested_dict['free_trial_end_date'] + ", " + days_left
    
    # If user's company did pay latest month
    if user_team_channeL_paid_latest_month == True:
      free_trial_ends_info = ''
    # ------------------------ Page Pre Load Check - Redirect Check - Free Trial / Latest Month Paid END ------------------------


    user_slack_email_permission_granted = user_nested_dict['user_slack_email_permission_granted']
    if user_slack_email_permission_granted == True or user_slack_email_permission_granted == 'True':
      return redirect('/dashboard', code=302)
    # ------------------------ Page Load User Pre Checks END ------------------------


    # ------------------------ Check Form Response START ------------------------
    user_consent_form_response = request.form.get('email-consent-name')
    if user_consent_form_response != 'agree':
      localhost_print_function('=========================================== /notifications/email/permission/processing Page END ===========================================')
      return redirect('/notifications/email/permission', code=302)
    else:
      # user_slack_email_permission_granted = user_nested_dict['user_slack_email_permission_granted']
      user_slack_email_permission_granted = True
    # ------------------------ Check Form Response END ------------------------


    # ------------------------ Update Postgres DB START ------------------------
    user_uuid = user_nested_dict['user_uuid']
    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()
    # Update Postgres DB
    output_message = update_account_consent_email_function(postgres_connection, postgres_cursor, user_uuid)
    # ------------------------ Update Postgres DB END ------------------------


    # ------------------------ Update Redis DB START ------------------------
    # Get cookie value from browser
    get_cookie_value_from_browser = check_cookie_browser_function()
    # Change Redis value
    user_nested_dict['user_slack_email_permission_granted'] = user_slack_email_permission_granted
    # Connect to redis database pool (no need to close)
    redis_connection = redis_connect_to_database_function()
    # Upload dictionary to redis based on cookies
    redis_connection.set(get_cookie_value_from_browser, json.dumps(user_nested_dict).encode('utf-8'))
    # ------------------------ Update Redis DB END ------------------------


    # ------------------------ Send Account Created Email START ------------------------
    slack_db_uuid = user_nested_dict['user_uuid']
    user_email = user_nested_dict['user_email']
    slack_authed_user_real_full_name = user_nested_dict['user_full_name']
    user_channel_name = user_nested_dict['slack_channel_name']

    output_email = user_email
    output_subject_line = 'Triviafy Account Created - Next Steps'
    output_message_content = f"Hi {slack_authed_user_real_full_name},\n\nThank you for creating an account with Triviafy.\n\n'What about my team?' In order to get the rest of your team setup with Triviafy please share with them:\n1) The attached Slack Setup Guide PDF file and\n2) The name of the Slack channel you are using for Triviafy: '{user_channel_name}' \n\nYou will be notified by email and Slack once your team's weekly quiz is open.\n\nBest,\nRob\n\nTriviafy your workspace."
    output_message_content_str_for_db = output_message_content

    # email_sent_successfully = send_email_template_function(output_email, output_subject_line, output_message_content)
    email_sent_successfully = send_email_with_slack_setup_attachment_template_function(output_email, output_subject_line, output_message_content)

    # Insert this sent email into DB
    uuid_email_sent = create_uuid_function('email_sent_')
    email_sent_timestamp = create_timestamp_function()
    # - - -
    email_sent_search_category = 'Account Created'
    uuid_quiz = None
    # - - -
    output_message = insert_triviafy_emails_sent_table_function(postgres_connection, postgres_cursor, uuid_email_sent, email_sent_timestamp, slack_db_uuid, email_sent_search_category, uuid_quiz, output_message_content_str_for_db)

    # Close Connection to Postgres DB
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Send Account Created Email END ------------------------


  except:
    localhost_print_function('page load except error hit')
    localhost_print_function('=========================================== /notifications/email/permission/processing Page END ===========================================')
    return redirect('/logout', code=302)
    # return redirect('/', code=302)


  
  localhost_print_function('=========================================== /notifications/email/permission/processing Page END ===========================================')
  return redirect('/dashboard', code=302)