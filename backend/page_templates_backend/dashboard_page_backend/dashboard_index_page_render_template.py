# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.utils.latest_quiz_utils.make_company_latest_quiz import make_company_latest_quiz_function
from backend.utils.latest_quiz_utils.get_latest_company_quiz_if_exists import get_latest_company_quiz_if_exists_function
from backend.utils.latest_quiz_utils.supporting_make_company_latest_quiz_utils.convert_question_ids_from_string_to_arr import convert_question_ids_from_string_to_arr_function
from backend.db.queries.select_queries.select_company_quiz_questions_individually import select_company_quiz_questions_individually_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.page_templates_backend.dashboard_page_backend.get_user_saved_quiz_question_answers import get_user_saved_quiz_question_answers_function
from backend.utils.datetime_utils.check_if_quiz_is_past_due_datetime import check_if_quiz_is_past_due_datetime_function

# -------------------------------------------------------------- App Setup
dashboard_index_page_render_template = Blueprint("dashboard_index_page_render_template", __name__, static_folder="static", template_folder="templates")
@dashboard_index_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@dashboard_index_page_render_template.route("/dashboard", methods=['GET','POST'])
def dashboard_index_page_render_template_function():
  print('=========================================== /dashboard Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  # ------------------------ Check if user is signed in START ------------------------
  try:
    user_nested_dict = check_if_user_login_through_cookies_function()
    
    # Get user information from the nested dict
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']
    user_uuid = user_nested_dict['user_uuid']
    user_company_name = user_nested_dict['user_company_name']
    user_channel_name = user_nested_dict['slack_channel_name']

    # ------------------------ 1/2 Get Latest Quiz Data START ------------------------
    latest_company_quiz_object = get_latest_company_quiz_if_exists_function(user_nested_dict)
    
    if latest_company_quiz_object != None:
      print('- - - - -')
      print('Pulled the latest company quiz from DB')
      print('- - - - -')
      # Assign the variables for the HTML inputs based on the pulled object
      uuid_quiz = latest_company_quiz_object[0]                                     # str
      quiz_timestamp_created = latest_company_quiz_object[1].strftime('%Y-%m-%d')   # str
      quiz_slack_team_id = latest_company_quiz_object[2]                            # str
      quiz_slack_channel_id = latest_company_quiz_object[3]                         # str
      quiz_start_date = latest_company_quiz_object[4].strftime('%Y-%m-%d')          # str
      quiz_start_day_of_week = latest_company_quiz_object[5]                        # str
      quiz_start_time = latest_company_quiz_object[6]                               # str
      quiz_end_date = latest_company_quiz_object[7].strftime('%Y-%m-%d')            # str
      quiz_end_day_of_week = latest_company_quiz_object[8]                          # str
      quiz_end_time = latest_company_quiz_object[9]                                 # str
      quiz_number_of_questions = latest_company_quiz_object[10]                     # int
      quiz_question_ids_str = latest_company_quiz_object[11]                        # str
      quiz_company_quiz_count = latest_company_quiz_object[12]                      # int

      # Quiz Question ID's have to be converted from 1 string to an arr
      quiz_question_ids_arr = convert_question_ids_from_string_to_arr_function(quiz_question_ids_str)   # list
    # ------------------------ 1/2 Get Latest Quiz Data END ------------------------

    
    # ------------------------ 2/2 Make Latest Quiz Data START ------------------------
    """
    NOTE: This should be a job, the quiz gets made automatically outside of the dashboard because what if no user from the company channel combo logs on for 3 weeks, then quiz will never get made
    """
    if latest_company_quiz_object == None:
      latest_company_quiz_object = make_company_latest_quiz_function(user_nested_dict)
      print('- - - - -')
      print('Made the latest company quiz from scratch')
      print('- - - - -')

      if latest_company_quiz_object != None:
        # Assign the variables for the HTML inputs based on the pulled object
        uuid_quiz = latest_company_quiz_object[0]                 # str
        quiz_timestamp_created = latest_company_quiz_object[1]    # str
        quiz_slack_team_id = latest_company_quiz_object[2]        # str
        quiz_slack_channel_id = latest_company_quiz_object[3]     # str
        quiz_start_date = latest_company_quiz_object[4]           # str
        quiz_start_day_of_week = latest_company_quiz_object[5]    # str
        quiz_start_time = latest_company_quiz_object[6]           # str
        quiz_end_date = latest_company_quiz_object[7]             # str
        quiz_end_day_of_week = latest_company_quiz_object[8]      # str
        quiz_end_time = latest_company_quiz_object[9]             # str
        quiz_number_of_questions = latest_company_quiz_object[10] # int
        quiz_question_ids_arr = latest_company_quiz_object[11]    # list
        quiz_company_quiz_count = latest_company_quiz_object[12]  # int
    # ------------------------ 2/2 Make Latest Quiz Data END ------------------------


    # ------------------------ If Quiz Is Past Due Date START ------------------------
    quiz_is_past_due_date = check_if_quiz_is_past_due_datetime_function(quiz_end_date, quiz_end_time)
    if quiz_is_past_due_date == True:
      return redirect('/dashboard/quiz/past/due', code=302)
    # ------------------------ If Quiz Is Past Due Date END ------------------------


    # ------------------------ Pull the Quiz Questions START ------------------------
    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()

    # Pull the quiz questions by id's found in the quiz_question_ids_arr
    quiz_questions_obj_arr_of_dicts = []
    for question_id in quiz_question_ids_arr:
      # Select query to pull the questions in the correct order
      quiz_question_dict = select_company_quiz_questions_individually_function(postgres_connection, postgres_cursor, question_id)
      quiz_questions_obj_arr_of_dicts.append(quiz_question_dict[0])


    # Add current question count to the dictionary for html
    current_count = 0
    for i in quiz_questions_obj_arr_of_dicts:
      current_count += 1
      i['quiz_question_number'] = current_count
    # ------------------------ Pull the Quiz Questions END ------------------------


    # ------------------------ Pull the Quiz User Answers If Exist START ------------------------
    user_quiz_saved_answers_dict = get_user_saved_quiz_question_answers_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz)

    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Pull the Quiz User Answers If Exist END ------------------------


    # ------------------------ Add User Autofill Answers to Obj START ------------------------
    if user_quiz_saved_answers_dict != None:
      for i in quiz_questions_obj_arr_of_dicts:
        i['users_most_recent_submitted_answer'] = user_quiz_saved_answers_dict[i['question_uuid']]
    else:
      for i in quiz_questions_obj_arr_of_dicts:
        i['users_most_recent_submitted_answer'] = ''
    # ------------------------ Add User Autofill Answers to Obj END ------------------------


  except:
    print('=========================================== /dashboard Page END ===========================================')
    return redirect('/', code=302)
  # ------------------------ Check if user is signed in END ------------------------


  
  print('=========================================== /dashboard Page END ===========================================')
  return render_template('dashboard_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          user_team_latest_quiz_number_to_html = quiz_company_quiz_count,
                          quiz_end_time_to_html = quiz_end_time,
                          quiz_end_day_of_week_to_html = quiz_end_day_of_week,
                          quiz_end_date_to_html = quiz_end_date,
                          quiz_questions_obj_arr_of_dicts_html = quiz_questions_obj_arr_of_dicts)