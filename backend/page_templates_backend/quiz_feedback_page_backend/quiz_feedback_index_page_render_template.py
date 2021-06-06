# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_latest_feedback_user_uuid import select_latest_feedback_user_uuid_function
from datetime import date, datetime

# -------------------------------------------------------------- App Setup
quiz_feedback_index_page_render_template = Blueprint("quiz_feedback_index_page_render_template", __name__, static_folder="static", template_folder="templates")
@quiz_feedback_index_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@quiz_feedback_index_page_render_template.route("/quiz/team/feedback", methods=['GET','POST'])
def quiz_feedback_index_page_render_template_function():
  print('=========================================== /quiz/team/feedback Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  # ------------------------ Check if user is signed in START ------------------------
  try:
    user_nested_dict = check_if_user_login_through_cookies_function()

    user_uuid = user_nested_dict['user_uuid']
    user_company_name = user_nested_dict['user_company_name']
    user_channel_name = user_nested_dict['slack_channel_name']

    
    # ------------------------ Check if user already submitted feedback today START ------------------------
    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()
    
    # Select latest feedback data based on uuid
    latest_feedback_from_user_uuid = select_latest_feedback_user_uuid_function(postgres_connection, postgres_cursor, user_uuid)

    if latest_feedback_from_user_uuid != 'User has not submitted any feedback yet today' and latest_feedback_from_user_uuid[0] != None:
      today = date.today().strftime('%Y-%m-%d')
      latest_feedback_from_user_uuid = latest_feedback_from_user_uuid[0].strftime('%Y-%m-%d')
      
      if today == latest_feedback_from_user_uuid:
        print('user already submitted feedback today')
        print('=========================================== /quiz/team/feedback Page END ===========================================')
        return redirect('/quiz/team/feedback/submit', code=302)
    
    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Check if user already submitted feedback today END ------------------------

    
  except:
    print('=========================================== /quiz/team/feedback Page END ===========================================')
    return redirect('/', code=302)
  # ------------------------ Check if user is signed in END ------------------------

  
  print('=========================================== /quiz/team/feedback Page END ===========================================')
  return render_template('quiz_feedback_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name)