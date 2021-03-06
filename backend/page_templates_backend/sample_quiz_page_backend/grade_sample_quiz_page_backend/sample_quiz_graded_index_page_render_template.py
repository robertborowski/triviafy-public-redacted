# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_queries_triviafy_sample_questions_table.select_triviafy_sample_questions_table_all import select_triviafy_sample_questions_table_all_function
from backend.db.queries.select_queries.select_queries_triviafy_all_questions_table.select_company_quiz_questions_individually import select_company_quiz_questions_individually_function
from backend.utils.sanitize_user_inputs.sanitize_quiz_question_user_answer_text import sanitize_quiz_question_user_answer_text_function
from backend.utils.grade_user_answers_utils.check_if_admin_answer_is_arr_of_answers import check_if_admin_answer_is_arr_of_answers_function
from backend.utils.grade_user_answers_utils.check_user_answer_vs_admin_answer import check_user_answer_vs_admin_answer_function
from backend.utils.sanitize_page_outputs.sanitize_page_output_company_name import sanitize_page_output_company_name_function
from backend.utils.free_trial_period_utils.check_if_free_trial_period_is_expired_days_left import check_if_free_trial_period_is_expired_days_left_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
from backend.utils.check_paid_latest_month_utils.check_if_user_team_channel_combo_paid_latest_month import check_if_user_team_channel_combo_paid_latest_month_function

# -------------------------------------------------------------- App Setup
sample_quiz_graded_index_page_render_template = Blueprint("sample_quiz_graded_index_page_render_template", __name__, static_folder="static", template_folder="templates")
@sample_quiz_graded_index_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@sample_quiz_graded_index_page_render_template.route("/sample/quiz/graded", methods=['GET','POST'])
def sample_quiz_graded_index_page_render_template_function():
  localhost_print_function('=========================================== /sample/quiz/graded Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  try:
    # ------------------------ Page Pre Load Check - User Logged In Through Cookies START ------------------------
    # Check if user logged in through cookies
    user_nested_dict = check_if_user_login_through_cookies_function()
    # ------------------------ Page Pre Load Check - User Logged In Through Cookies END ------------------------

    # ------------------------ Page Pre Load Check - Redirect Check - Free Trial / Latest Month Paid START ------------------------
    # Check if user Team/Channel combo paid the latest month
    user_team_channeL_paid_latest_month = check_if_user_team_channel_combo_paid_latest_month_function(user_nested_dict)
    
    # If user's company did not pay latest month
    if user_team_channeL_paid_latest_month == False:
      # Check if user free trial is expired
      user_nested_dict = check_if_free_trial_period_is_expired_days_left_function(user_nested_dict)
      if user_nested_dict == None or user_nested_dict == True:
        return redirect('/subscription', code=302)

      days_left = str(user_nested_dict['trial_period_days_left_int']) + " days left."
      if user_nested_dict['trial_period_days_left_int'] == 1:
        days_left = str(user_nested_dict['trial_period_days_left_int']) + " day left."

      free_trial_ends_info = "Free Trial Ends: " + user_nested_dict['free_trial_end_date'] + ", " + days_left
    
    # If user's company did pay latest month
    if user_team_channeL_paid_latest_month == True:
      free_trial_ends_info = ''
    # ------------------------ Page Pre Load Check - Redirect Check - Free Trial / Latest Month Paid END ------------------------

    # ------------------------ Page Pre Load Check - Redirect Check - Permission Granted START ------------------------
    user_slack_email_permission_granted = user_nested_dict['user_slack_email_permission_granted']
    if user_slack_email_permission_granted == False or user_slack_email_permission_granted == 'False':
      return redirect('/notifications/email/permission', code=302)
    # ------------------------ Page Pre Load Check - Redirect Check - Permission Granted END ------------------------

    # ------------------------ Page Pre Load Check - Redirect Check - New User Questionnaire Answered START ------------------------
    user_slack_new_user_questionnaire_answered = user_nested_dict['user_slack_new_user_questionnaire_answered']
    if user_slack_new_user_questionnaire_answered == False or user_slack_new_user_questionnaire_answered == 'False':
      return redirect('/new/user/questionnaire', code=302)
    # ------------------------ Page Pre Load Check - Redirect Check - New User Questionnaire Answered END ------------------------


    # ------------------------ Page Company Info START ------------------------
    user_company_name = user_nested_dict['user_company_name']
    user_company_name = sanitize_page_output_company_name_function(user_company_name)
    user_channel_name = user_nested_dict['slack_channel_name']
    # ------------------------ Page Company Info END ------------------------
    
    # Get additional variables
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']


    # ------------------------ Sanitize User Inputs START ------------------------
    user_answer_to_q1 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_1'))
    user_answer_to_q2 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_2'))
    user_answer_to_q3 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_3'))
    user_answer_to_q4 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_4'))
    user_answer_to_q5 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_5'))
    user_answer_to_q6 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_6'))
    user_answer_to_q7 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_7'))
    user_answer_to_q8 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_8'))
    user_answer_to_q9 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_9'))
    user_answer_to_q10 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_10'))

    if user_answer_to_q1 == None or user_answer_to_q2 == None or user_answer_to_q3 == None or user_answer_to_q4 == None or user_answer_to_q5 == None:
      localhost_print_function('inputs are not valid')
      localhost_print_function('=========================================== /dashboard/user/submit/quiz Page END ===========================================')
      return redirect('/dashboard', code=302)
    
    # Add user responses to an arr
    user_sample_answer_responses_arr = []
    user_sample_answer_responses_arr.append(user_answer_to_q1)
    user_sample_answer_responses_arr.append(user_answer_to_q2)
    user_sample_answer_responses_arr.append(user_answer_to_q3)
    user_sample_answer_responses_arr.append(user_answer_to_q4)
    user_sample_answer_responses_arr.append(user_answer_to_q5)
    user_sample_answer_responses_arr.append(user_answer_to_q6)
    user_sample_answer_responses_arr.append(user_answer_to_q7)
    user_sample_answer_responses_arr.append(user_answer_to_q8)
    user_sample_answer_responses_arr.append(user_answer_to_q9)
    user_sample_answer_responses_arr.append(user_answer_to_q10)
    # ------------------------ Sanitize User Inputs END ------------------------


    # ------------------------ Open Connections START ------------------------
    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()
    # ------------------------ Open Connections END ------------------------


    # ------------------------ Get Sample Question UUIDs START ------------------------
    # Get sample questions from DB as arr
    sample_question_uuids_arr = select_triviafy_sample_questions_table_all_function(postgres_connection, postgres_cursor)
    # ------------------------ Get Quiz Settings Info END ------------------------


    # ------------------------ Get Quiz Question Arr of Dicts START ------------------------
    sample_questions_arr_of_dicts = []
    for sample_question_uuid in sample_question_uuids_arr:
      sample_question_dict = select_company_quiz_questions_individually_function(postgres_connection, postgres_cursor, sample_question_uuid)
      sample_questions_arr_of_dicts.append(sample_question_dict[0])
    # ------------------------ Get Quiz Question Arr of Dicts END ------------------------


    # ------------------------ Add Current Question Count To Dict START ------------------------
    current_count = 0
    for i in sample_questions_arr_of_dicts:
      current_count += 1
      i['quiz_question_number'] = current_count
    # ------------------------ Add Current Question Count To Dict END ------------------------


    # ------------------------ Add Current User Answer To Dict START ------------------------
    current_answer_index = 0
    for i in sample_questions_arr_of_dicts:
      i['user_quiz_question_answer'] = user_sample_answer_responses_arr[current_answer_index]
      current_answer_index += 1
    # ------------------------ Add Current Question Count To Dict END ------------------------


    # ------------------------ Close Connections START ------------------------
    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Close Connections END ------------------------


    # ------------------------ Grade Sample Quiz - User Answers START ------------------------
    for dict in sample_questions_arr_of_dicts:
      # Assign variables from dict
      question_admin_correct_answer = dict['question_answers_list']
      question_user_answer_attempt = dict['user_quiz_question_answer']

      # Check if admin answer is an array of multiple answers
      question_has_multiple_answers, question_admin_correct_answers_arr = check_if_admin_answer_is_arr_of_answers_function(question_admin_correct_answer)
      # ------------------------ Run Checks For All Answers START ------------------------
      # If there are multiple answers
      if question_has_multiple_answers == True:
        for i in question_admin_correct_answers_arr:
          # Run all checks against the user-answer-attempt vs the admin-correct-answer
          result_grading_checks = check_user_answer_vs_admin_answer_function(i, question_user_answer_attempt)
          if result_grading_checks == True:
            dict['user_quiz_question_result'] = str(result_grading_checks)
            break
          else:
            dict['user_quiz_question_result'] = str(result_grading_checks)

      if question_has_multiple_answers == False:
        # Run all checks against the user-answer-attempt vs the admin-correct-answer
        result_grading_checks = check_user_answer_vs_admin_answer_function(question_admin_correct_answer, question_user_answer_attempt)
        if result_grading_checks == True:
          dict['user_quiz_question_result'] = str(result_grading_checks)
        else:
          dict['user_quiz_question_result'] = str(result_grading_checks)
      # ------------------------ Run Checks For All Answers END ------------------------
    # ------------------------ Grade Sample Quiz - User Answers END ------------------------


    # ------------------------ Get Total Correct Answers START ------------------------
    total_questions_for_quiz = len(sample_questions_arr_of_dicts)
    total_correct_answers_for_quiz = 0
    for dict in sample_questions_arr_of_dicts:
      if dict['user_quiz_question_result'] == True or dict['user_quiz_question_result'] == 'True':
        total_correct_answers_for_quiz += 1
    # ------------------------ Get Total Correct Answers END ------------------------
    

  except:
    localhost_print_function('page load except error hit')
    localhost_print_function('=========================================== /sample/quiz/graded Page END ===========================================')
    return redirect('/logout', code=302)
    # return redirect('/', code=302)

  
  localhost_print_function('=========================================== /sample/quiz/graded Page END ===========================================')
  return render_template('sample_quiz_page_templates/graded_sample_quiz_page_templates/graded_sample_quiz_index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          quiz_questions_obj_arr_of_dicts_html = sample_questions_arr_of_dicts,
                          total_questions_for_quiz_to_html = total_questions_for_quiz,
                          total_correct_answers_for_quiz_to_html = total_correct_answers_for_quiz,
                          free_trial_ends_info_to_html = free_trial_ends_info)