# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.utils.uuid_and_timestamp.create_timestamp import create_timestamp_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.insert_queries.insert_triviafy_waitlist_create_question_table import insert_triviafy_waitlist_create_question_table_function
from backend.db.queries.select_queries.select_triviafy_waitlist_create_question_table_check_if_uuid_exists import select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function

# -------------------------------------------------------------- App Setup
waitlist_create_question_add_to_database_processing = Blueprint("waitlist_create_question_add_to_database_processing", __name__, static_folder="static", template_folder="templates")
@waitlist_create_question_add_to_database_processing.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@waitlist_create_question_add_to_database_processing.route("/create/question/user/waitlist/processing", methods=['GET','POST'])
def waitlist_create_question_add_to_database_processing_function():
  """Returns /create/question/user/waitlist/processing page"""
  print('=========================================== /create/question/user/waitlist/processing Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  # ------------------------ Check if user is signed in START ------------------------
  try:
    user_nested_dict = check_if_user_login_through_cookies_function()
    user_email = user_nested_dict['user_email']
    user_uuid = user_nested_dict['user_uuid']
  except:
    print('=========================================== /create/question/user/waitlist/processing Page END ===========================================')
    return redirect('/', code=302)
  # ------------------------ Check if user is signed in END ------------------------


  # ------------------------ Check if user is already on this waitlist START ------------------------
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()
  
  if_uuid_exists = select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function(postgres_connection, postgres_cursor, user_uuid)

  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)

  if if_uuid_exists == 'User already exists in db table':
    print(if_uuid_exists)
    print('redirecting user to the confirm waitlist page')
    print('=========================================== /create/question/user/waitlist/processing Page END ===========================================')
    return redirect('/create/question/user/waitlist/confirm', code=302)
  # ------------------------ Check if user is already on this waitlist END ------------------------
  
  
  # ------------------------ Create additional DB variables START ------------------------
  waitlist_create_question_uuid = create_uuid_function('wait_quest_')
  waitlist_create_question_timestamp = create_timestamp_function()
  # ------------------------ Create additional DB variables END ------------------------


  # ------------------------ Add user uuid to create question waitlist database START ------------------------
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()

  # DB insert attempt
  insert_triviafy_waitlist_create_question_table_function(postgres_connection, postgres_cursor, waitlist_create_question_uuid, waitlist_create_question_timestamp, user_uuid)

  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
  # ------------------------ Add user uuid to create question waitlist database END ------------------------

  print('=========================================== /create/question/user/waitlist/processing Page END ===========================================')
  print('redirecting user to the confirm waitlist page')
  return redirect('/create/question/user/waitlist/confirm', code=302)