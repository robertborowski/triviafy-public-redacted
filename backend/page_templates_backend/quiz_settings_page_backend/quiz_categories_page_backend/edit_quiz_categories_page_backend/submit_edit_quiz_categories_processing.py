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
from backend.utils.quiz_categories_utils.edit_quiz_categories_validate_user_inputs import edit_quiz_categories_validate_user_inputs_function
from backend.db.queries.select_queries.select_queries_triviafy_all_questions_table.select_triviafy_all_questions_table_all_unique_categories import select_triviafy_all_questions_table_all_unique_categories_function
from backend.db.queries.update_queries.update_queries_triviafy_categories_selected_table.update_edit_quiz_categories import update_edit_quiz_categories_function

# -------------------------------------------------------------- App Setup
submit_edit_quiz_categories_processing = Blueprint("submit_edit_quiz_categories_processing", __name__, static_folder="static", template_folder="templates")
@submit_edit_quiz_categories_processing.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@submit_edit_quiz_categories_processing.route("/categories/edit/processing", methods=['GET','POST'])
def submit_edit_quiz_categories_processing_function():
  localhost_print_function('=========================================== /categories/edit/processing Page START ===========================================')
  
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

    # ------------------------ Get User Form Checkbox Values START ------------------------
    # Select All Category Check
    user_form_categories_selected_select_all_checkbox = request.form.get('select_all_category_checkbox_name')
    if user_form_categories_selected_select_all_checkbox != None and user_form_categories_selected_select_all_checkbox != 'select_all_categories':
      localhost_print_function('=========================================== /categories/edit/processing Page END ===========================================')
      return redirect('/categories', code=302)

    # Deselect All Category Check
    user_form_categories_selected_deselect_all_checkbox = request.form.get('deselect_all_category_checkbox_name')
    if user_form_categories_selected_deselect_all_checkbox != None and user_form_categories_selected_deselect_all_checkbox != 'deselect_all_categories':
      localhost_print_function('=========================================== /categories/edit/processing Page END ===========================================')
      return redirect('/categories', code=302)

    # Categories that are not Select All or Deselect All
    user_form_categories_selected_arr = request.form.getlist('category_checkbox_name')
    validate_user_form_categories_selected_arr = edit_quiz_categories_validate_user_inputs_function(user_form_categories_selected_arr)
    if validate_user_form_categories_selected_arr == False:
      localhost_print_function('=========================================== /categories/edit/processing Page END ===========================================')
      return redirect('/categories', code=302)
    # ------------------------ Get User Form Checkbox Values END ------------------------


    # ------------------------ Connect to Postgres DB START ------------------------
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()
    # ------------------------ Connect to Postgres DB END ------------------------
    
    
    # ------------------------ Logic Selected Pre DB Update START ------------------------
    categories_to_push_to_db_str = ''
    caps_exceptions_set = {'sql'}
    
    # If other categories were checked
    if user_form_categories_selected_select_all_checkbox == None and user_form_categories_selected_deselect_all_checkbox == None:
      if len(user_form_categories_selected_arr) >= 1:
        categories_to_push_to_db_arr = []
        for i_category in user_form_categories_selected_arr:
          i_category_with_space = i_category.replace('_',' ')
          if i_category_with_space in caps_exceptions_set:
            i_category_with_caps = i_category_with_space.upper()
            categories_to_push_to_db_arr.append(i_category_with_caps)
          else:
            i_category_with_title = i_category_with_space.title()
            categories_to_push_to_db_arr.append(i_category_with_title)
          categories_to_push_to_db_arr = sorted(categories_to_push_to_db_arr)
          categories_to_push_to_db_str = ",".join(categories_to_push_to_db_arr)

    # If select all was checked
    if user_form_categories_selected_select_all_checkbox == 'select_all_categories':
      categories_to_push_to_db_str = 'All Categories'

    # If deselect all was checked
    if user_form_categories_selected_deselect_all_checkbox == 'deselect_all_categories':
      categories_to_push_to_db_str = 'Pop Culture'
    # ------------------------ Logic Selected Pre DB Update END ------------------------

    
    # ------------------------ Update DB New Categories START ------------------------
    if categories_to_push_to_db_str != None and categories_to_push_to_db_str != '':
      output_message = update_edit_quiz_categories_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, categories_to_push_to_db_str)
    # ------------------------ Update DB New Categories END ------------------------
    

    # ------------------------ Close Postgres DB START ------------------------
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Close Postgres DB END ------------------------
    
  except:
    localhost_print_function('page load except error hit')
    localhost_print_function('=========================================== /categories/edit/processing Page END ===========================================')
    return redirect('/logout', code=302)
    # return redirect('/', code=302)

  
  localhost_print_function('=========================================== /categories/edit/processing Page END ===========================================')
  return redirect('/categories', code=302)