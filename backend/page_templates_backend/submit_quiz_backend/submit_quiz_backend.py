  # -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.utils.sanitize_user_inputs.sanitize_quiz_question_user_answer_text import sanitize_quiz_question_user_answer_text_function

# -------------------------------------------------------------- App Setup
submit_quiz_backend = Blueprint("submit_quiz_backend", __name__, static_folder="static", template_folder="templates")
@submit_quiz_backend.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@submit_quiz_backend.route("/dashboard/user/submit/quiz", methods=['GET','POST'])
def submit_quiz_backend_function():
  """Submits quiz"""
  print('=========================================== /dashboard/user/submit/quiz Page START ===========================================')
  
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


    # ------------------------ Sanitize User Inputs START ------------------------
    user_answer_to_q1 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_1'))
    user_answer_to_q2 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_2'))
    user_answer_to_q3 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_3'))
    user_answer_to_q4 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_4'))
    user_answer_to_q5 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_5'))
    try:
      user_answer_to_q6 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_6'))
      user_answer_to_q7 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_7'))
      user_answer_to_q8 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_8'))
      user_answer_to_q9 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_9'))
      user_answer_to_q10 = sanitize_quiz_question_user_answer_text_function(request.form.get('user_input_quiz_question_answer_10'))
    except:
      user_answer_to_q6 = 'Only 5 question quiz'
      user_answer_to_q7 = 'Only 5 question quiz'
      user_answer_to_q8 = 'Only 5 question quiz'
      user_answer_to_q9 = 'Only 5 question quiz'
      user_answer_to_q10 = 'Only 5 question quiz'

    if user_answer_to_q1 == None or user_answer_to_q2 == None or user_answer_to_q3 == None or user_answer_to_q4 == None or user_answer_to_q5 == None or user_answer_to_q6 == None or user_answer_to_q7 == None or user_answer_to_q8 == None or user_answer_to_q9 == None or user_answer_to_q10 == None:
      print('input not valid')
      print('=========================================== /dashboard/user/submit/quiz Page END ===========================================')
      return redirect('/dashboard', code=302)
    # ------------------------ Sanitize User Inputs END ------------------------
  
    print('- - - - - - -')
    print(user_answer_to_q1)
    print(user_answer_to_q2)
    print(user_answer_to_q3)
    print(user_answer_to_q4)
    print(user_answer_to_q5)
    print(user_answer_to_q6)
    print(user_answer_to_q7)
    print(user_answer_to_q8)
    print(user_answer_to_q9)
    print(user_answer_to_q10)
    print('- - - - - - -')


  except:
    print('=========================================== /dashboard/user/submit/quiz Page END ===========================================')
    return redirect('/', code=302)
  # ------------------------ Check if user is signed in END ------------------------


  
  print('=========================================== /dashboard/user/submit/quiz Page END ===========================================')
  return redirect('/dashboard', code=302)