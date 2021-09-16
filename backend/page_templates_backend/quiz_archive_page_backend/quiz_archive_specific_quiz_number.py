# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_queries_triviafy_quiz_master_table.select_quiz_uuid_from_quiz_master_table import select_quiz_uuid_from_quiz_master_table_function
from datetime import datetime
from backend.utils.latest_quiz_utils.supporting_make_company_latest_quiz_utils.convert_question_ids_from_string_to_arr import convert_question_ids_from_string_to_arr_function
from backend.db.queries.select_queries.select_queries_triviafy_all_questions_table.select_triviafy_all_questions_table_question_info import select_triviafy_all_questions_table_question_info_function
from backend.db.queries.select_queries.select_queries_triviafy_quiz_answers_master_table.select_triviafy_quiz_answers_master_table_user_answer import select_triviafy_quiz_answers_master_table_user_answer_function
from backend.utils.sanitize_page_outputs.sanitize_page_output_company_name import sanitize_page_output_company_name_function
from backend.utils.free_trial_period_utils.check_if_free_trial_period_is_expired_days_left import check_if_free_trial_period_is_expired_days_left_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
from backend.utils.check_paid_latest_month_utils.check_if_user_team_channel_combo_paid_latest_month import check_if_user_team_channel_combo_paid_latest_month_function

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
  localhost_print_function('=========================================== /quiz/archive/<html_variable_quiz_number> Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  try:
    # ------------------------ Page Load User Pre Checks START ------------------------
    # Check if user logged in through cookies
    user_nested_dict = check_if_user_login_through_cookies_function()

    # ------------------------ Check If Free Trial / Latest Month Paid START ------------------------
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
    # ------------------------ Check If Free Trial / Latest Month Paid END ------------------------
    # ------------------------ Page Load User Pre Checks END ------------------------
    
    # ------------------------ Page Company Info START ------------------------
    user_company_name = user_nested_dict['user_company_name']
    user_company_name = sanitize_page_output_company_name_function(user_company_name)
    user_channel_name = user_nested_dict['slack_channel_name']
    # ------------------------ Page Company Info END ------------------------
    
    # Get additional variables
    user_uuid = user_nested_dict['user_uuid']
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']
    int_quiz_number = int(html_variable_quiz_number)


    # ------------------------ Get Info From triviafy_quiz_master_table START ------------------------
    # ------------------------ Open Connections START ------------------------
    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()
    # ------------------------ Open Connections END ------------------------

    # From Quiz Number link selected, get Quiz UUID and Question UUID's 
    link_selected_quiz_master_table_arr = select_quiz_uuid_from_quiz_master_table_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, int_quiz_number)
    
    # Assign Variables from DB pull
    link_selected_uuid_quiz = link_selected_quiz_master_table_arr[0]
    link_selected_question_ids_str = convert_question_ids_from_string_to_arr_function(link_selected_quiz_master_table_arr[1])   # list
    link_selected_company_quiz_count = link_selected_quiz_master_table_arr[8]
    link_selected_quiz_master_string_start = link_selected_quiz_master_table_arr[2].strftime("%Y-%m-%d") + ', ' + link_selected_quiz_master_table_arr[3] + ', ' + link_selected_quiz_master_table_arr[4]
    link_selected_quiz_master_string_end = link_selected_quiz_master_table_arr[5].strftime("%Y-%m-%d") + ', ' + link_selected_quiz_master_table_arr[6] + ', ' + link_selected_quiz_master_table_arr[7]
    
    # Put the pulled values into dict
    link_selected_quiz_archive_intro_dict = {
      'company_quiz_count' : link_selected_company_quiz_count,
      'quiz_master_string_start' : link_selected_quiz_master_string_start,
      'quiz_master_string_end' : link_selected_quiz_master_string_end
    }

    # Check to make sure archive quiz number is correct
    if int_quiz_number != link_selected_company_quiz_count:
      localhost_print_function('quiz link int does not match pulled quiz int number')
      localhost_print_function('=========================================== /quiz/archive/<html_variable_quiz_number> Page END ===========================================')
      return redirect('/', code=302)
    # ------------------------ Get Info From triviafy_quiz_master_table END ------------------------


    
    # ------------------------ Get Info From triviafy_all_questions_table START ------------------------
    pull_info_all_questions_table_arr_of_dicts = []
    for question_id in link_selected_question_ids_str:
      pulled_item_arr_of_dict = select_triviafy_all_questions_table_question_info_function(postgres_connection, postgres_cursor, question_id)
      pulled_dict = pulled_item_arr_of_dict[0]
      pull_info_all_questions_table_arr_of_dicts.append(pulled_dict)
    # ------------------------ Get Info From triviafy_all_questions_table END ------------------------
    
    
    
    # ------------------------ Get Info From triviafy_quiz_answers_master_table START ------------------------
    pull_info_quiz_answers_master_table_answer_dict = {}
    pull_info_quiz_answers_master_table_result_dict = {}
    for question_id in link_selected_question_ids_str:
      pulled_item_arr = select_triviafy_quiz_answers_master_table_user_answer_function(postgres_connection, postgres_cursor, question_id, user_uuid)
      pull_info_quiz_answers_master_table_answer_dict[pulled_item_arr[0]] = pulled_item_arr[1].replace("_", " ")
      pull_info_quiz_answers_master_table_result_dict[pulled_item_arr[0]] = pulled_item_arr[2]
    # ------------------------ Get Info From triviafy_quiz_answers_master_table END ------------------------


    # ------------------------ Map User Submitted Answer To Quiz Question Obj START ------------------------
    question_number_count = 1
    # Loop through array of dicts
    for dict in pull_info_all_questions_table_arr_of_dicts:
      dict['user_quiz_question_answer'] = pull_info_quiz_answers_master_table_answer_dict[dict['question_uuid']]
      dict['user_quiz_question_result'] = pull_info_quiz_answers_master_table_result_dict[dict['question_uuid']]
      dict['quiz_question_number'] = question_number_count
      question_number_count += 1
    # ------------------------ Map User Submitted Answer To Quiz Question Obj END ------------------------


    # ------------------------ Close Connections START ------------------------
    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Close Connections END ------------------------


    # ------------------------ Get Total Correct Answers START ------------------------
    total_questions_for_quiz = len(pull_info_all_questions_table_arr_of_dicts)
    total_correct_answers_for_quiz = 0
    for dict in pull_info_all_questions_table_arr_of_dicts:
      if dict['user_quiz_question_result'] == True or dict['user_quiz_question_result'] == 'True':
        total_correct_answers_for_quiz += 1
    # ------------------------ Get Total Correct Answers END ------------------------


  except:
    localhost_print_function('page load except error hit')
    localhost_print_function('=========================================== /quiz/archive/<html_variable_quiz_number> Page END ===========================================')
    return redirect('/logout', code=302)
    # return redirect('/', code=302)


  
  localhost_print_function('=========================================== /quiz/archive/<html_variable_quiz_number> Page END ===========================================')
  return render_template('quiz_archive_page_templates/quiz_archive_specific_version.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          link_selected_quiz_archive_intro_dict_to_html = link_selected_quiz_archive_intro_dict,
                          pull_info_all_questions_table_arr_of_dicts_to_html = pull_info_all_questions_table_arr_of_dicts,
                          total_questions_for_quiz_to_html = total_questions_for_quiz,
                          total_correct_answers_for_quiz_to_html = total_correct_answers_for_quiz,
                          free_trial_ends_info_to_html = free_trial_ends_info)