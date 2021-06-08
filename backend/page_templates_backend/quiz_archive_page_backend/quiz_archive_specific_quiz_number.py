# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_quiz_uuid_from_quiz_master_table import select_quiz_uuid_from_quiz_master_table_function
from datetime import datetime

# -------------------------------------------------------------- App Setup
quiz_archive_specific_quiz_number = Blueprint("quiz_archive_specific_quiz_number", __name__, static_folder="static", template_folder="templates")
@quiz_archive_specific_quiz_number.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@quiz_archive_specific_quiz_number.route("/quiz/archive/<html_variable_quiz_number>", methods=['GET','POST'])
def quiz_archive_specific_quiz_number_function(html_variable_quiz_number):
  print('=========================================== /quiz/archive/<html_variable_quiz_number> Page START ===========================================')
  
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
    int_quiz_number = int(html_variable_quiz_number)


    # ------------------------ Get Specific Quiz Version Information START ------------------------
    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()

    uuid_quiz_link_selected_arr = select_quiz_uuid_from_quiz_master_table_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, int_quiz_number)
    uuid_quiz_link_selected = uuid_quiz_link_selected_arr[0]
    # ------------------------ Get Specific Quiz Version Information END ------------------------


    # ------------------------ Get User Submitted Info From DB For Quiz UUID START ------------------------
    # ------------------------ Get User Submitted Info From DB For Quiz UUID END ------------------------


    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)


  except:
    print('except error hit')
    print('=========================================== /quiz/archive/<html_variable_quiz_number> Page END ===========================================')
    return redirect('/', code=302)
  # ------------------------ Check if user is signed in END ------------------------


  
  print('=========================================== /quiz/archive/<html_variable_quiz_number> Page END ===========================================')
  return render_template('quiz_archive_page_templates/quiz_archive_specific_version.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name)