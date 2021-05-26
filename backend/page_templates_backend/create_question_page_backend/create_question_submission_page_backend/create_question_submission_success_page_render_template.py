# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.create_question_queries.select_all_questions_created_by_owner_email import select_all_questions_created_by_owner_email_function
import os

# -------------------------------------------------------------- App Setup
create_question_submission_success_page_render_template = Blueprint("create_question_submission_success_page_render_template", __name__, static_folder="static", template_folder="templates")
@create_question_submission_success_page_render_template.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@create_question_submission_success_page_render_template.route("/create/question/user/form/submit/success", methods=['GET','POST'])
def create_question_submission_success_page_render_template_function():
  """Returns /create/question/user/form/submit/success page"""
  print('=========================================== /create/question/user/form/submit/success Page START ===========================================')
  
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
    user_email = user_nested_dict['user_email']
  except:
    print('=========================================== /create/question/user/form/submit/success Page END ===========================================')
    return redirect('/', code=302)
  # ------------------------ Check if user is signed in END ------------------------


  # ------------------------ Check create question accesss START ------------------------
  # Get personal email
  personal_email = os.environ.get('PERSONAL_EMAIL')

  # If user does not have access to create questions then redirect to waitlist page
  if user_email != personal_email:
    print('redirecting to the create question wait list page!')
    print('=========================================== /create/question/user/form/submit/success Page END ===========================================')
    return redirect('/create/question/user/waitlist', code=302)
  # ------------------------ Check create question accesss END ------------------------

  
  # ------------------------ Pull created questions from user START ------------------------
  # Pull all questions submitted by this user
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()

  # Pull info from db
  user_all_questions_submitted_dict = select_all_questions_created_by_owner_email_function(postgres_connection, postgres_cursor, user_email)
  
  # print('- - - - - - - - - - -')
  # for i in user_all_questions_submitted_dict:
  #   print(i)
  #   print('- - -')
  # print('- - - - - - - - - - -')

  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
  # ------------------------ Pull created questions from user END ------------------------

  
  print('=========================================== /create/question/user/form/submit/success Page END ===========================================')
  return render_template('create_question_page_templates/create_question_submission_page_templates/create_question_submission_success.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          user_email_to_html = user_email,
                          user_all_submitted_questions_html = user_all_questions_submitted_dict)