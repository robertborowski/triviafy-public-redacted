# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.utils.sanitize_page_outputs.sanitize_page_output_company_name import sanitize_page_output_company_name_function
from backend.utils.free_trial_period_utils.check_if_free_trial_period_is_expired_days_left import check_if_free_trial_period_is_expired_days_left_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
from backend.utils.check_paid_latest_month_utils.check_if_user_team_channel_combo_paid_latest_month import check_if_user_team_channel_combo_paid_latest_month_function
from backend.db.queries.select_queries.select_queries_triviafy_all_questions_table.select_triviafy_all_questions_table_all_unique_categories import select_triviafy_all_questions_table_all_unique_categories_function
from backend.db.queries.select_queries.select_queries_triviafy_categories_selected_table.select_current_categories_team_channel_combo import select_current_categories_team_channel_combo_function

# -------------------------------------------------------------- App Setup
edit_quiz_categories_index_page_render_template = Blueprint("edit_quiz_categories_index_page_render_template", __name__, static_folder="static", template_folder="templates")
@edit_quiz_categories_index_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@edit_quiz_categories_index_page_render_template.route("/categories/edit", methods=['GET','POST'])
def edit_quiz_categories_index_page_render_template_function():
  localhost_print_function('=========================================== /categories/edit Page START ===========================================')
  
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

    # ------------------------ Page Pre Load Check - Redirect Check - Permission Granted START ------------------------
    user_slack_email_permission_granted = user_nested_dict['user_slack_email_permission_granted']
    if user_slack_email_permission_granted == False or user_slack_email_permission_granted == 'False':
      return redirect('/notifications/email/permission', code=302)
    # ------------------------ Page Pre Load Check - Redirect Check - Permission Granted END ------------------------

    # ------------------------ Page Pre Load Check - Redirect Check - New User Questionnaire Answered START ------------------------
    user_slack_new_user_questionnaire_answered = user_nested_dict['user_slack_new_user_questionnaire_answered']
    if user_slack_new_user_questionnaire_answered == False or user_slack_new_user_questionnaire_answered == 'False':
      return redirect('/new/user/questionnaire', code=302)
    # ------------------------ Page Pre Load Check - Redirect Check - New User Questionnaire Answered END ------------------------

    # ------------------------ Page Company Info START ------------------------
    user_company_name = user_nested_dict['user_company_name']
    user_company_name = sanitize_page_output_company_name_function(user_company_name)
    user_channel_name = user_nested_dict['slack_channel_name']
    # ------------------------ Page Company Info END ------------------------
    
    # Get additional variables
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']


    # ------------------------ Connect to Postgres DB START ------------------------
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()
    # ------------------------ Connect to Postgres DB END ------------------------


    # ------------------------ Currently Selected Categories START ------------------------
    company_current_selected_categories_str = select_current_categories_team_channel_combo_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id)
    company_current_selected_categories_arr = company_current_selected_categories_str.split(',')

    # Make a temp set to make checking/separating quicker
    temp_set_checker = {''}
    for i in company_current_selected_categories_arr:
      temp_set_checker.add(i)
    temp_set_checker.remove('')

    # Create Arr of Dict for selected categories
    company_current_selected_categories_arr_of_dicts = []
    for word in company_current_selected_categories_arr:
      temp_dict = {}
      temp_dict['category'] = word
      temp_dict['category_response_tracking'] = word.replace(" ", "_").lower()
      company_current_selected_categories_arr_of_dicts.append(temp_dict)
    # ------------------------ Currently Selected Categories END ------------------------


    # ------------------------ Currently Deselected Categories START ------------------------
    # ------------------------ Pull unique categories from SQL DB START ------------------------
    unique_categories_arr_pulled_from_db = select_triviafy_all_questions_table_all_unique_categories_function(postgres_connection, postgres_cursor)
    # ------------------------ Pull unique categories from SQL DB END ------------------------
    # ------------------------ Loop Create Arr of Dicts START ------------------------
    company_current_deselected_categories_arr_of_dicts = []
    for i_unique_categories in unique_categories_arr_pulled_from_db:
      i_unique_categories_zero = i_unique_categories[0]
      i_unique_categories_zero_split_arr = i_unique_categories_zero.split(',')
      if len(i_unique_categories_zero_split_arr) > 1:
        for word in i_unique_categories_zero_split_arr:
          temp_dict = {}
          word = word.strip()
          if word not in temp_set_checker:
            temp_dict['category'] = word
            temp_dict['category_response_tracking'] = word.replace(" ", "_").lower()
            company_current_deselected_categories_arr_of_dicts.append(temp_dict)
      else:
        temp_dict = {}
        word = i_unique_categories_zero_split_arr[0]
        if word not in temp_set_checker:
          temp_dict['category'] = word
          temp_dict['category_response_tracking'] = word.replace(" ", "_").lower()
          company_current_deselected_categories_arr_of_dicts.append(temp_dict)
    # ------------------------ Loop Create Arr of Dicts END ------------------------
    # ------------------------ Currently Deselected Categories END ------------------------


    # ------------------------ Close Postgres DB START ------------------------
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Close Postgres DB END ------------------------
    
  except:
    localhost_print_function('page load except error hit')
    localhost_print_function('=========================================== /categories/edit Page END ===========================================')
    return redirect('/logout', code=302)
    # return redirect('/', code=302)

  
  localhost_print_function('=========================================== /categories/edit Page END ===========================================')
  return render_template('quiz_settings_page_templates/quiz_categories_page_templates/edit_quiz_categories_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          free_trial_ends_info_to_html = free_trial_ends_info,
                          company_current_selected_categories_arr_of_dicts_to_html = company_current_selected_categories_arr_of_dicts,
                          company_current_deselected_categories_arr_of_dicts_to_html = company_current_deselected_categories_arr_of_dicts)