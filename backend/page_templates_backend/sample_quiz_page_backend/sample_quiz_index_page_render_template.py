# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_triviafy_sample_questions_table_all import select_triviafy_sample_questions_table_all_function
from backend.db.queries.select_queries.select_company_quiz_questions_individually import select_company_quiz_questions_individually_function
from backend.utils.sanitize_page_outputs.sanitize_page_output_company_name import sanitize_page_output_company_name_function
from backend.utils.free_trial_period_utils.check_if_free_trial_period_is_expired_days_left import check_if_free_trial_period_is_expired_days_left_function

# -------------------------------------------------------------- App Setup
sample_quiz_index_page_render_template = Blueprint("sample_quiz_index_page_render_template", __name__, static_folder="static", template_folder="templates")
@sample_quiz_index_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@sample_quiz_index_page_render_template.route("/sample/quiz", methods=['GET','POST'])
def sample_quiz_index_page_render_template_function():
  print('=========================================== /sample/quiz Page START ===========================================')
  
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
    # ------------------------ Page Load User Pre Checks END ------------------------

    user_company_name = user_nested_dict['user_company_name']
    user_company_name = sanitize_page_output_company_name_function(user_company_name)
    user_channel_name = user_nested_dict['slack_channel_name']

    # Get Company name and channel name (slack ID's)
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']


    # ------------------------ Open Connections START ------------------------
    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()
    # ------------------------ Open Connections END ------------------------


    # ------------------------ Get Sample Question UUIDs START ------------------------
    # Get quiz settings from DB as arr
    sample_question_uuids_arr = select_triviafy_sample_questions_table_all_function(postgres_connection, postgres_cursor)
    # ------------------------ Get Quiz Settings Info END ------------------------


    # ------------------------ Get Quiz Question Arr of Dicts START ------------------------
    sample_questions_arr_of_dicts = []
    for sample_question_uuid in sample_question_uuids_arr:
      sample_question_dict = select_company_quiz_questions_individually_function(postgres_connection, postgres_cursor, sample_question_uuid)
      sample_questions_arr_of_dicts.append(sample_question_dict[0])
    # ------------------------ Get Quiz Question Arr of Dicts END ------------------------


    # ------------------------ Add Current Question Count To Dict START ------------------------
    current_count = 0
    for i in sample_questions_arr_of_dicts:
      current_count += 1
      i['quiz_question_number'] = current_count
    # ------------------------ Add Current Question Count To Dict END ------------------------


    # ------------------------ Close Connections START ------------------------
    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Close Connections END ------------------------
    
  except:
    print('=========================================== /sample/quiz Page END ===========================================')
    return redirect('/', code=302)

  
  print('=========================================== /sample/quiz Page END ===========================================')
  return render_template('sample_quiz_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          quiz_questions_obj_arr_of_dicts_html = sample_questions_arr_of_dicts)