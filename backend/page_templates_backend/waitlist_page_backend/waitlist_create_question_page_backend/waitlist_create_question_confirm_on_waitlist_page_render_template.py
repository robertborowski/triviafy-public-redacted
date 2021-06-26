# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_triviafy_waitlist_create_question_table_check_if_uuid_exists import select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function
from backend.utils.free_trial_period_utils.check_if_free_trial_period_is_expired_days_left import check_if_free_trial_period_is_expired_days_left_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- App Setup
waitlist_create_question_confirm_on_waitlist_page_render_template = Blueprint("waitlist_create_question_confirm_on_waitlist_page_render_template", __name__, static_folder="static", template_folder="templates")
@waitlist_create_question_confirm_on_waitlist_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@waitlist_create_question_confirm_on_waitlist_page_render_template.route("/create/question/user/waitlist/confirm", methods=['GET','POST'])
def waitlist_create_question_confirm_on_waitlist_page_render_template_function():
  localhost_print_function('=========================================== /create/question/user/waitlist/confirm Page START ===========================================')
  
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

    user_uuid = user_nested_dict['user_uuid']

  except:
    localhost_print_function('page load except error hit')
    localhost_print_function('=========================================== /create/question/user/waitlist/confirm Page END ===========================================')
    return redirect('/logout', code=302)
    # return redirect('/', code=302)


  # ------------------------ Check if user is already on this waitlist START ------------------------
  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()
  
  if_uuid_exists = select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function(postgres_connection, postgres_cursor, user_uuid)

  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)

  if if_uuid_exists != True:
    localhost_print_function('redirecting user to the waitlist signup page')
    localhost_print_function('=========================================== /create/question/user/waitlist/confirm Page END ===========================================')
    return redirect('/create/question/user/waitlist', code=302)
  # ------------------------ Check if user is already on this waitlist END ------------------------


  # ------------------------ Return confirm page START ------------------------
  return render_template('waitlist_page_templates/waitlist_create_question_page_template/waitlist_create_question_confirm_on_waitlist.html')
  # ------------------------ Return confirm page END ------------------------