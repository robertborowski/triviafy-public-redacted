# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_company_quiz_archive_all_graded_quizzes import select_company_quiz_archive_all_graded_quizzes_function
from datetime import datetime

# -------------------------------------------------------------- App Setup
quiz_archive_page_render_template = Blueprint("quiz_archive_page_render_template", __name__, static_folder="static", template_folder="templates")
@quiz_archive_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@quiz_archive_page_render_template.route("/quiz/archive", methods=['GET','POST'])
def quiz_archive_page_render_template_function():
  print('=========================================== /quiz/archive Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  # ------------------------ Check if user is signed in START ------------------------
  try:
    user_nested_dict = check_if_user_login_through_cookies_function()
    
    # Get user information from the nested dict
    user_company_name = user_nested_dict['user_company_name']
    user_channel_name = user_nested_dict['slack_channel_name']
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']


    # ------------------------ Get All Graded Quizzes For Company START ------------------------
    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()

    company_quiz_archive_all_graded_quizzes_arr = select_company_quiz_archive_all_graded_quizzes_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id)

    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Get All Graded Quizzes For Company END ------------------------


    # ------------------------ Transpose Results Into Arr of Dict START ------------------------
    company_quiz_archive_all_graded_quizzes_arr_of_dicts = []

    for i in company_quiz_archive_all_graded_quizzes_arr:
      # Create Variables for the dict
      quiz_master_string_start = i[2].strftime("%Y-%m-%d") + ', ' + i[3] + ', ' + i[4]
      quiz_master_string_end = i[5].strftime("%Y-%m-%d") + ', ' + i[6] + ', ' + i[7]
      
      temp_dict = {
        # 'uuid_quiz' : i[0],
        'company_quiz_count' : i[1],
        # 'quiz_start_date' : i[2],
        # 'quiz_start_day_of_week' : i[3],
        # 'quiz_start_time' : i[4],
        'quiz_master_string_start' : quiz_master_string_start,
        # 'quiz_end_date' : i[5],
        # 'quiz_end_day_of_week' : i[6],
        # 'quiz_end_time' : i[7],
        'quiz_master_string_end' : quiz_master_string_end,
        'quiz_number_of_questions' : i[8],
        'user_display_name_winner' : i[9]
      }
      company_quiz_archive_all_graded_quizzes_arr_of_dicts.append(temp_dict)
    # ------------------------ Transpose Results Into Arr of Dict END ------------------------


  except:
    print('except error hit')
    print('=========================================== /quiz/archive Page END ===========================================')
    return redirect('/', code=302)
  # ------------------------ Check if user is signed in END ------------------------


  
  print('=========================================== /quiz/archive Page END ===========================================')
  return render_template('quiz_archive_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          company_quiz_archive_all_graded_quizzes_arr_of_dicts_to_html = company_quiz_archive_all_graded_quizzes_arr_of_dicts)