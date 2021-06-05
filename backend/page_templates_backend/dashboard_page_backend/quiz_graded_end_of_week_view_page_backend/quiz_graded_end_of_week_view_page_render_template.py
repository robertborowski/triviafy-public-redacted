# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.utils.latest_quiz_utils.check_if_latest_quiz_is_graded_utils.check_if_latest_quiz_is_graded import check_if_latest_quiz_is_graded_function
from backend.utils.latest_quiz_utils.get_latest_company_quiz_if_exists import get_latest_company_quiz_if_exists_function
from backend.utils.latest_quiz_utils.supporting_make_company_latest_quiz_utils.convert_question_ids_from_string_to_arr import convert_question_ids_from_string_to_arr_function
from backend.utils.datetime_utils.check_if_quiz_is_past_due_datetime import check_if_quiz_is_past_due_datetime_function

# -------------------------------------------------------------- App Setup
quiz_graded_end_of_week_view_page_render_template = Blueprint("quiz_graded_end_of_week_view_page_render_template", __name__, static_folder="static", template_folder="templates")
@quiz_graded_end_of_week_view_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@quiz_graded_end_of_week_view_page_render_template.route("/dashboard/quiz/results", methods=['GET','POST'])
def quiz_graded_end_of_week_view_page_render_template_function():
  """Returns /dashboard/quiz/results page"""
  print('=========================================== /dashboard/quiz/results Page START ===========================================')
  
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
    # Get user information from the nested dict
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']

    # ------------------------ Double Check If Quiz Is Graded START ------------------------
    # ------------------------ Get Latest Quiz Data START ------------------------
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
    # ------------------------ Get Latest Quiz Data END ------------------------


    # ------------------------ Double Check If Quiz Is Past Due Date START ------------------------
    quiz_is_past_due_date = check_if_quiz_is_past_due_datetime_function(quiz_end_date, quiz_end_time)
    # ------------------------ Double Check If Quiz Is Past Due Date END ------------------------
    if quiz_is_past_due_date == True:
      # ------------------------ Double Check If Quiz Is Graded START ------------------------
      latest_quiz_is_graded_check = check_if_latest_quiz_is_graded_function(slack_workspace_team_id, slack_channel_id, uuid_quiz)
      if latest_quiz_is_graded_check != True:
        print('Latest quiz is not yet fully graded.')
        print('=========================================== /dashboard/quiz/results Page END ===========================================')
        return redirect('/', code=302)
      # ------------------------ Double Check If Quiz Is Graded END ------------------------


  except:
    print('except error hit')
    print('=========================================== /dashboard/quiz/results Page END ===========================================')
    return redirect('/', code=302)
  # ------------------------ Check if user is signed in END ------------------------


  
  print('=========================================== /dashboard/quiz/results Page END ===========================================')
  return render_template('dashboard_page_templates/quiz_graded_end_of_week_view_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name)