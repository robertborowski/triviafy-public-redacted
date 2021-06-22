# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_company_quiz_archive_all_graded_quizzes import select_company_quiz_archive_all_graded_quizzes_function
from backend.utils.sanitize_page_outputs.sanitize_page_output_company_name import sanitize_page_output_company_name_function

# -------------------------------------------------------------- App Setup
quiz_archive_none_yet_page_render_template = Blueprint("quiz_archive_none_yet_page_render_template", __name__, static_folder="static", template_folder="templates")
@quiz_archive_none_yet_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@quiz_archive_none_yet_page_render_template.route("/quiz/archive", methods=['GET','POST'])
def quiz_archive_none_yet_page_render_template_function():
  print('=========================================== /quiz/archive/none Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  # ------------------------ Check if user is signed in START ------------------------
  try:
    user_nested_dict = check_if_user_login_through_cookies_function()
    
    # Get user information from the nested dict
    user_company_name = user_nested_dict['user_company_name']
    user_company_name = sanitize_page_output_company_name_function(user_company_name)
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


    # ------------------------ If No Quizzes Are In Archive For Company START ------------------------
    if company_quiz_archive_all_graded_quizzes_arr != None:
      print('Company-team does have quiz archives, redirecting to correct page')
      print('=========================================== /quiz/archive/none Page END ===========================================')
      return redirect('/quiz/archive', code=302)
    # ------------------------ If No Quizzes Are In Archive For Company END ------------------------


  except:
    print('except error hit')
    print('=========================================== /quiz/archive/none Page END ===========================================')
    return redirect('/', code=302)
  # ------------------------ Check if user is signed in END ------------------------


  
  print('=========================================== /quiz/archive/none Page END ===========================================')
  return render_template('quiz_archive_page_templates/quiz_archive_none_yet_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name)