# -------------------------------------------------------------- Imports
from flask import Blueprint, redirect, request
import os
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.uuid_and_timestamp.create_timestamp import create_timestamp_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
from backend.utils.sanitize_user_inputs.sanitize_simple_text_input import sanitize_simple_text_input_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.utils.check_paid_latest_month_utils.check_if_user_team_channel_combo_paid_latest_month import check_if_user_team_channel_combo_paid_latest_month_function
from backend.utils.free_trial_period_utils.check_if_free_trial_period_is_expired_days_left import check_if_free_trial_period_is_expired_days_left_function
from backend.db.queries.select_queries.select_queries_triviafy_new_user_questionnaire_response_table.select_new_user_questionnaire_response import select_new_user_questionnaire_response_function
from backend.db.queries.insert_queries.insert_queries_triviafy_new_user_questionnaire_response_table.insert_user_new_questionnaire_response import insert_user_new_questionnaire_response_function
from backend.db.queries.update_queries.update_queries_triviafy_new_user_questionnaire_response_table.update_account_questionnarie_complete import update_account_questionnarie_complete_function
from backend.utils.cached_login.check_cookie_browser import check_cookie_browser_function
from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
import json

# -------------------------------------------------------------- App Setup
new_user_questionnaire_submit_processing = Blueprint("new_user_questionnaire_submit_processing", __name__, static_folder="static", template_folder="templates")
@new_user_questionnaire_submit_processing.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@new_user_questionnaire_submit_processing.route("/new/user/questionnaire/processing", methods=['GET','POST'])
def new_user_questionnaire_submit_processing_function():
  localhost_print_function('=========================================== /new/user/questionnaire/processing Page START ===========================================')


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

    # ------------------------ Page Pre Load Check - Redirect Check - Permission Granted START ------------------------
    user_slack_email_permission_granted = user_nested_dict['user_slack_email_permission_granted']
    if user_slack_email_permission_granted == False or user_slack_email_permission_granted == 'False':
      return redirect('/notifications/email/permission', code=302)
    # ------------------------ Page Pre Load Check - Redirect Check - Permission Granted END ------------------------


    # ------------------------ Declare database variables START ------------------------
    # Additional variables for database
    questionnaire_uuid = create_uuid_function('questionnaire_')
    questionnaire_timestamp = create_timestamp_function()
    
    user_slack_uuid = user_nested_dict['user_uuid']
    user_slack_team_id = user_nested_dict['slack_team_id']
    user_slack_channel_id = user_nested_dict['slack_channel_id']
    # ------------------------ Declare database variables END ------------------------


    # ------------------------ Connect to Database - Postgres START ------------------------
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()
    # ------------------------ Connect to Database - Postgres END ------------------------


    # ------------------------ Check If User/Team/Channel Response Already in DB START ------------------------
    user_team_channel_response_exists = select_new_user_questionnaire_response_function(postgres_connection, postgres_cursor, user_slack_uuid, user_slack_team_id, user_slack_channel_id)
    if user_team_channel_response_exists != None:
      localhost_print_function('user response already exists in DB')
      # ------------------------ Update Login Table Bool START ------------------------
      output_message = update_account_questionnarie_complete_function(postgres_connection, postgres_cursor, user_slack_uuid)
      # ------------------------ Update Login Table Bool END ------------------------
      # ------------------------ Update Redis DB START ------------------------
      if user_nested_dict['user_slack_new_user_questionnaire_answered'] == False:
        # Get cookie value from browser
        get_cookie_value_from_browser = check_cookie_browser_function()
        # Change Redis value
        user_nested_dict['user_slack_new_user_questionnaire_answered'] = True
        # Connect to redis database pool (no need to close)
        redis_connection = redis_connect_to_database_function()
        # Upload dictionary to redis based on cookies
        redis_connection.set(get_cookie_value_from_browser, json.dumps(user_nested_dict).encode('utf-8'))
        # ------------------------ Update Redis DB END ------------------------
      localhost_print_function('=========================================== /new/user/questionnaire/processing Page END ===========================================')
      return redirect('/', code=302)
    # ------------------------ Check If User/Team/Channel Response Already in DB END ------------------------


    # ------------------------ Close Connection to Database - Postgres START ------------------------
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Close Connection to Database - Postgres END ------------------------


    # ------------------------ Sanitize user inputs START ------------------------
    try:
      # Get/sanitize user inputs from form
      user_form_input_hear_about = sanitize_simple_text_input_function(request.form.get('user_input_hear_about'))
      user_form_input_gain_from = sanitize_simple_text_input_function(request.form.get('user_input_gain_from'))
      user_form_input_coworker_amount = sanitize_simple_text_input_function(request.form.get('user_input_coworker_amount'))
      user_form_input_if_competitor = sanitize_simple_text_input_function(request.form.get('user_input_if_competitor'))

    except:
      localhost_print_function('invalid url /new/user/questionnaire/processing Page')
      localhost_print_function('=========================================== /new/user/questionnaire/processing Page END ===========================================')
      return redirect('/', code=302)
    # ------------------------ Sanitize user inputs END ------------------------


    # ------------------------ Check sanitized results START ------------------------
    # Check if sanitized inputs are valid and if code can move on
    if user_form_input_hear_about == None or user_form_input_gain_from == None or user_form_input_coworker_amount == None or user_form_input_if_competitor == None:
      localhost_print_function('invalid inputs')
      localhost_print_function('=========================================== /new/user/questionnaire/processing Page END ===========================================')
      return redirect('/', code=302)
    # ------------------------ Check sanitized results END ------------------------


    # ------------------------ Connect to Database - Postgres START ------------------------
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()
    # ------------------------ Connect to Database - Postgres END ------------------------


    # ------------------------ Insert Into DB START ------------------------
    output_message = insert_user_new_questionnaire_response_function(postgres_connection, postgres_cursor, questionnaire_uuid, questionnaire_timestamp, user_slack_uuid, user_slack_team_id, user_slack_channel_id, user_form_input_hear_about, user_form_input_gain_from, user_form_input_coworker_amount, user_form_input_if_competitor)
    # ------------------------ Insert Into DB START ------------------------


    # ------------------------ Update Login Table Bool START ------------------------
    output_message = update_account_questionnarie_complete_function(postgres_connection, postgres_cursor, user_slack_uuid)
    # ------------------------ Update Login Table Bool END ------------------------


    # ------------------------ Close Connection to Database - Postgres START ------------------------
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Close Connection to Database - Postgres END ------------------------


    # ------------------------ Update Redis DB START ------------------------
    # Get cookie value from browser
    get_cookie_value_from_browser = check_cookie_browser_function()
    # Change Redis value
    user_nested_dict['user_slack_new_user_questionnaire_answered'] = True
    # Connect to redis database pool (no need to close)
    redis_connection = redis_connect_to_database_function()
    # Upload dictionary to redis based on cookies
    redis_connection.set(get_cookie_value_from_browser, json.dumps(user_nested_dict).encode('utf-8'))
    # ------------------------ Update Redis DB END ------------------------


  except:
    localhost_print_function('page load except error hit /new/user/questionnaire/processing Page')
    localhost_print_function('=========================================== /new/user/questionnaire/processing Page END ===========================================')
    return redirect('/logout', code=302)

  
  localhost_print_function('=========================================== /new/user/questionnaire/processing Page END ===========================================')
  return redirect('/', code=302)