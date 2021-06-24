# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.utils.latest_quiz_utils.get_latest_company_quiz_if_exists import get_latest_company_quiz_if_exists_function
from backend.utils.latest_quiz_utils.supporting_make_company_latest_quiz_utils.get_next_weeks_dates_data_dict import get_next_weeks_dates_data_dict_function
from backend.db.queries.select_queries.select_company_quiz_settings import select_company_quiz_settings_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.utils.latest_quiz_utils.get_previous_week_company_quiz_if_exists import get_previous_week_company_quiz_if_exists_function
from backend.utils.sanitize_page_outputs.sanitize_page_output_company_name import sanitize_page_output_company_name_function
from backend.utils.free_trial_period_utils.check_if_free_trial_period_is_expired_days_left import check_if_free_trial_period_is_expired_days_left_function

# -------------------------------------------------------------- App Setup
quiz_no_latest_quiz_yet_page_render_template = Blueprint("quiz_no_latest_quiz_yet_page_render_template", __name__, static_folder="static", template_folder="templates")
@quiz_no_latest_quiz_yet_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@quiz_no_latest_quiz_yet_page_render_template.route("/dashboard/quiz/first/pending", methods=['GET','POST'])
def quiz_no_latest_quiz_yet_page_render_template_function():
  print('=========================================== /dashboard/quiz/first/pending Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  try:
    # ------------------------ Page Load User Pre Checks START ------------------------
    # Check if user logged in through cookies
    user_nested_dict = check_if_user_login_through_cookies_function()

    # Check if user free trial is expired
    user_nested_dict = check_if_free_trial_period_is_expired_days_left_function(user_nested_dict)
    if user_nested_dict == None or user_nested_dict == True:
      return redirect('/subscription', code=302)

    days_left = str(user_nested_dict['trial_period_days_left_int']) + " days left."
    if user_nested_dict['trial_period_days_left_int'] == 1:
      days_left = str(user_nested_dict['trial_period_days_left_int']) + " day left."

    free_trial_ends_info = "Free Trial Ends: " + user_nested_dict['free_trial_end_date'] + ", " + days_left
    # ------------------------ Page Load User Pre Checks END ------------------------
    
    
    # Get user information from the nested dict
    user_company_name = user_nested_dict['user_company_name']
    user_company_name = sanitize_page_output_company_name_function(user_company_name)
    user_channel_name = user_nested_dict['slack_channel_name']

    # Get Company name and channel name (slack ID's)
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']

    # ------------------------ If Latest Company Quiz Obj None START ------------------------
    # Make sure that there is no latest company quiz if someone goes to this URL
    latest_company_quiz_object = get_latest_company_quiz_if_exists_function(user_nested_dict)

    if latest_company_quiz_object != None:
      print('latest_company_quiz_object is != None. Redirecting to dashboard')
      print('=========================================== /dashboard/quiz/first/pending Page END ===========================================')
      return redirect('/dashboard', code=302)
    # ------------------------ If Latest Company Quiz Obj None END ------------------------


    # ------------------------ Check If Previous Week is None too START ------------------------
    if latest_company_quiz_object == None:
      # Check if there is a previous week quiz made
      previous_week_company_quiz_object = get_previous_week_company_quiz_if_exists_function(user_nested_dict)
      if previous_week_company_quiz_object != None:
        print('previous_week_company_quiz_object is != None. Redirecting to dashboard')
        print('=========================================== /dashboard/quiz/first/pending Page END ===========================================')
        return redirect('/dashboard', code=302)
    # ------------------------ Check if This Is Companies First Every Quiz END ------------------------
    # ------------------------ Check If Previous Week is None too END ------------------------


    # ------------------------ Get The Company Quiz Settings START ------------------------
    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()

    # Get quiz settings from DB as arr
    quiz_settings_arr = select_company_quiz_settings_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id)
    # Assign the arr values
    company_quiz_settings_last_updated_timestamp = quiz_settings_arr[1]
    company_quiz_settings_start_day = quiz_settings_arr[2]
    company_quiz_settings_start_time = quiz_settings_arr[3]
    company_quiz_settings_end_day = quiz_settings_arr[4]
    company_quiz_settings_end_time = quiz_settings_arr[5]
    company_quiz_settings_questions_per_quiz = quiz_settings_arr[6]

    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Get The Company Quiz Settings END ------------------------


    # ------------------------ Get Next Week's Dates Dict START ------------------------
    next_week_dates_dict = get_next_weeks_dates_data_dict_function()
    company_first_quiz_will_be_created_start_day = company_quiz_settings_start_day
    company_first_quiz_will_be_created_start_date = next_week_dates_dict[company_quiz_settings_start_day]
    # ------------------------ Get Next Week's Dates Dict End ------------------------


  except:
    print('page load except error hit')
    print('=========================================== /dashboard/quiz/first/pending Page END ===========================================')
    return redirect('/logout', code=302)
    # return redirect('/', code=302)


  
  print('=========================================== /dashboard/quiz/first/pending Page END ===========================================')
  return render_template('dashboard_page_templates/quiz_no_latest_quiz_yet_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          company_first_quiz_will_be_created_start_day_to_html = company_first_quiz_will_be_created_start_day,
                          company_first_quiz_will_be_created_start_date_to_html = company_first_quiz_will_be_created_start_date,
                          free_trial_ends_info_to_html = free_trial_ends_info)