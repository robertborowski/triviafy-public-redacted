# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_triviafy_sample_questions_table_all import select_triviafy_sample_questions_table_all_function
from backend.db.queries.select_queries.select_company_quiz_questions_individually import select_company_quiz_questions_individually_function
from backend.utils.sanitize_user_inputs.sanitize_quiz_question_user_answer_text import sanitize_quiz_question_user_answer_text_function
from backend.utils.grade_user_answers_utils.check_if_admin_answer_is_arr_of_answers import check_if_admin_answer_is_arr_of_answers_function
from backend.utils.grade_user_answers_utils.check_user_answer_vs_admin_answer import check_user_answer_vs_admin_answer_function
from backend.utils.sanitize_page_outputs.sanitize_page_output_company_name import sanitize_page_output_company_name_function

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
  print('=========================================== /sample/quiz/graded Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  # ------------------------ Check if user is signed in START ------------------------
  try:
    user_nested_dict = check_if_user_login_through_cookies_function()

    user_company_name = user_nested_dict['user_company_name']
    user_company_name = sanitize_page_output_company_name_function(user_company_name)
    user_channel_name = user_nested_dict['slack_channel_name']

    # Get Company name and channel name (slack ID's)
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']


    # ------------------------ Sanitize User Inputs START ------------------------
    user_answer_to_q1 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_1'))
    user_answer_to_q2 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_2'))
    user_answer_to_q3 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_3'))
    user_answer_to_q4 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_4'))
    user_answer_to_q5 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_5'))

    if user_answer_to_q1 == None or user_answer_to_q2 == None or user_answer_to_q3 == None or user_answer_to_q4 == None or user_answer_to_q5 == None:
      print('inputs are not valid')
      print('=========================================== /dashboard/user/submit/quiz Page END ===========================================')
      return redirect('/dashboard', code=302)
    
    # Add user responses to an arr
    user_sample_answer_responses_arr = []
    user_sample_answer_responses_arr.append(user_answer_to_q1)
    user_sample_answer_responses_arr.append(user_answer_to_q2)
    user_sample_answer_responses_arr.append(user_answer_to_q3)
    user_sample_answer_responses_arr.append(user_answer_to_q4)
    user_sample_answer_responses_arr.append(user_answer_to_q5)
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
    print('=========================================== /sample/quiz/graded Page END ===========================================')
    return redirect('/', code=302)
  # ------------------------ Check if user is signed in END ------------------------

  
  print('=========================================== /sample/quiz/graded Page END ===========================================')
  return render_template('sample_quiz_page_templates/graded_sample_quiz_page_templates/graded_sample_quiz_index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          quiz_questions_obj_arr_of_dicts_html = sample_questions_arr_of_dicts,
                          total_questions_for_quiz_to_html = total_questions_for_quiz,
                          total_correct_answers_for_quiz_to_html = total_correct_answers_for_quiz)