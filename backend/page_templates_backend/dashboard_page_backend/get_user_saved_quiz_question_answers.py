# -------------------------------------------------------------- Imports
from backend.db.queries.select_queries.select_user_quiz_question_answer_if_exists_autofill import select_user_quiz_question_answer_if_exists_autofill_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def get_user_saved_quiz_question_answers_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz):
  localhost_print_function('=========================================== get_user_saved_quiz_question_answers_function START ===========================================')
  
  user_quiz_question_answers_arr = select_user_quiz_question_answer_if_exists_autofill_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz)


  if user_quiz_question_answers_arr == None or user_quiz_question_answers_arr == []:
    localhost_print_function('no answers saved from this user on this quiz & question combo')
    localhost_print_function('=========================================== get_user_saved_quiz_question_answers_function END ===========================================')
    return None

  # Quiz Question and answer tuple
  user_quiz_question_id_and_answers_dict = {}
  for i in user_quiz_question_answers_arr:    
    # Get quiz question ID and the actual answer from select statement results
    # User answer in DB contains "_" between words for sanitation, change that back to spaces
    user_quiz_question_id_and_answers_dict[i[6]] = i[7].replace('_',' ')

  localhost_print_function('=========================================== get_user_saved_quiz_question_answers_function END ===========================================')
  return user_quiz_question_id_and_answers_dict