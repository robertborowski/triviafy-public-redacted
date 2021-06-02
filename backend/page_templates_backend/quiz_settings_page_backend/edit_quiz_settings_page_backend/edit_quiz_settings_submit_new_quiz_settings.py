# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.uuid_and_timestamp.create_timestamp import create_timestamp_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.queries.select_queries.select_company_quiz_settings import select_company_quiz_settings_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.utils.sanitize_user_inputs.sanitize_edit_quiz_setting_day import sanitize_edit_quiz_setting_day_function
from backend.utils.sanitize_user_inputs.sanitize_edit_quiz_setting_time import sanitize_edit_quiz_setting_time_function
from backend.utils.sanitize_user_inputs.sanitize_edit_quiz_setting_num_questions import sanitize_edit_quiz_setting_num_questions_function
from backend.db.queries.update_queries.update_edit_quiz_settings import update_edit_quiz_settings_function
from backend.utils.quiz_settings_page_utils.convert_form_results_to_db_inputs import convert_form_results_to_db_inputs_function

# -------------------------------------------------------------- App Setup
edit_quiz_settings_submit_new_quiz_settings = Blueprint("edit_quiz_settings_submit_new_quiz_settings", __name__, static_folder="static", template_folder="templates")
@edit_quiz_settings_submit_new_quiz_settings.before_request
def before_request():
  ""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@edit_quiz_settings_submit_new_quiz_settings.route("/quiz/team/settings/payment/admin/edit/submit/processing", methods=['GET','POST'])
def edit_quiz_settings_submit_new_quiz_settings_function():
  """Returns /quiz/team/settings/payment/admin/edit/submit/processing settings page"""
  print('=========================================== /quiz/team/settings/payment/admin/edit/submit/processing Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  # ------------------------ Check if user is signed in START ------------------------
  try:
    user_nested_dict = check_if_user_login_through_cookies_function()

    # Get Company name and channel name (slack ID's)
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']
    

    # ------------------------ Check if user is payment admin in START ------------------------
    # See if user is payment admin. If not then they cannot edit quiz settings
    user_payment_admin_status = user_nested_dict['user_is_payment_admin']
    if user_payment_admin_status != True:
      print('User is not a payment admin on their team/channel ID combo')
      print('=========================================== /quiz/team/settings/payment/admin/edit/submit/processing Page END ===========================================')
      return redirect('/quiz/team/settings', code=302)
    # ------------------------ Check if user is payment admin in END ------------------------


    # ------------------------ Get Quiz Settings Form Inputs START ------------------------
    # Get the user form data and sanitize it in the same line
    user_form_input_quiz_start_day = sanitize_edit_quiz_setting_day_function(request.form.get('edit-quiz-start-day'))
    user_form_input_quiz_start_time = sanitize_edit_quiz_setting_time_function(request.form.get('edit-quiz-start-time'))
    user_form_input_quiz_end_day = sanitize_edit_quiz_setting_day_function(request.form.get('edit-quiz-end-day'))
    user_form_input_quiz_end_time = sanitize_edit_quiz_setting_time_function(request.form.get('edit-quiz-end-time'))
    user_form_input_quiz_num_questions = sanitize_edit_quiz_setting_num_questions_function(request.form.get('edit-quiz-num-questions'))

    # ------------------------ Invalid Inputs START ------------------------
    if user_form_input_quiz_start_day == None or user_form_input_quiz_start_time == None or user_form_input_quiz_end_day == None or user_form_input_quiz_end_time == None or user_form_input_quiz_num_questions == None:
      print('=========================================== /quiz/team/settings/payment/admin/edit/submit/processing Page END ===========================================')
      return redirect('/', code=302)
    # ------------------------ Invalid Inputs END ------------------------

    # Change the form input str to an int
    if user_form_input_quiz_num_questions == 'five_questions':
      user_form_input_quiz_num_questions = 5
    if user_form_input_quiz_num_questions == 'ten_questions':
      user_form_input_quiz_num_questions = 10

    # ------------------------ Form Start End Logic START ------------------------
    # Logic behind the form, End Date/Time cannot be before Start Day/Time
    quiz_settings_logic_day_dict = {
      'monday' : 1,
      'tuesday' : 2,
      'wednesday' : 3
    }
    quiz_settings_logic_time_dict = {
      'nine_am' : 1,
      'ten_am' : 2,
      'eleven_am' : 3,
      'noon' : 4,
      'one_pm' : 5,
      'two_pm' : 6,
      'three_pm' : 7,
      'four_pm' : 8,
      'five_pm' : 9,
      'six_pm' : 10,
      'seven_pm' : 11
    }

    # Check if days make sense
    quiz_start_day_index = quiz_settings_logic_day_dict[user_form_input_quiz_start_day]
    quiz_end_day_index = quiz_settings_logic_day_dict[user_form_input_quiz_end_day]
    if quiz_end_day_index < quiz_start_day_index:
      # Switch start and end day
      temp_end_day = user_form_input_quiz_end_day
      user_form_input_quiz_end_day = user_form_input_quiz_start_day
      user_form_input_quiz_start_day = temp_end_day
    
    # Check if time is the same on the same day error
    if (user_form_input_quiz_start_time == user_form_input_quiz_end_time) and (user_form_input_quiz_start_day == user_form_input_quiz_end_day):
      print('quiz start/end time cannot be the same on the same day')
    
    # Check if quiz times make sense
    quiz_start_time_index = quiz_settings_logic_time_dict[user_form_input_quiz_start_time]
    quiz_end_time_index = quiz_settings_logic_time_dict[user_form_input_quiz_end_time]
    if (user_form_input_quiz_start_day == user_form_input_quiz_end_day) and (quiz_end_time_index < quiz_start_time_index):
      # Switch start and end time
      temp_end_time = user_form_input_quiz_end_time
      user_form_input_quiz_end_time = user_form_input_quiz_start_time
      user_form_input_quiz_start_time = temp_end_time
    # ------------------------ Form Start End Logic END ------------------------
    
    # ------------------------ Convert inputs to database friendly inputs START ------------------------
    converted_start_day, converted_start_time, converted_end_day, converted_end_time = convert_form_results_to_db_inputs_function(user_form_input_quiz_start_day, user_form_input_quiz_start_time, user_form_input_quiz_end_day, user_form_input_quiz_end_time)
    # ------------------------ Convert inputs to database friendly inputs END ------------------------
    # ------------------------ Get Quiz Settings Form Inputs END ------------------------


    # ------------------------ Get Current Quiz Settings DB Info START ------------------------
    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()

    # Get quiz settings from DB as arr
    quiz_settings_arr = select_company_quiz_settings_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id)
    # Assign the arr values
    uuid_company_quiz_settings = quiz_settings_arr[0]
    # ------------------------ Get Current Quiz Settings DB Info END ------------------------


    # ------------------------ Update Quiz Settings table in DB START ------------------------
    # New timestamp for edited quiz settings
    company_quiz_settings_last_updated_timestamp = create_timestamp_function()

    update_edit_quiz_settings_function(postgres_connection, postgres_cursor, company_quiz_settings_last_updated_timestamp, converted_start_day, converted_start_time, converted_end_day, converted_end_time, user_form_input_quiz_num_questions, uuid_company_quiz_settings)

    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Update Quiz Settings table in DB END ------------------------


  except:
    print('=========================================== /quiz/team/settings/payment/admin/edit/submit/processing Page END ===========================================')
    return redirect('/', code=302)
  # ------------------------ Check if user is signed in END ------------------------

  
  print('=========================================== /quiz/team/settings/payment/admin/edit/submit/processing Page END ===========================================')
  return redirect('/quiz/team/settings', code=302)