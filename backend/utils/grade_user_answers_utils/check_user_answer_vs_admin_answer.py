# -------------------------------------------------------------- Imports
import difflib
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def check_user_answer_vs_admin_answer_function(question_admin_correct_answer, question_user_answer_attempt):
  localhost_print_function('=========================================== check_user_answer_vs_admin_answer_function START ===========================================')
  
  # ------------------------ Pre Check Sanitize START ------------------------
  question_admin_correct_answer = question_admin_correct_answer.lower()
  question_admin_correct_answer = question_admin_correct_answer.strip()
  question_admin_correct_answer = question_admin_correct_answer.replace(' ','_')
  question_user_answer_attempt = question_user_answer_attempt.lower()
  # ------------------------ Pre Check Sanitize END ------------------------
  
  localhost_print_function('- - - - - - ATTEMPTING TO GRADE  - - - - - - -')
  localhost_print_function('question_admin_correct_answer: ' + question_admin_correct_answer)
  localhost_print_function('question_user_answer_attempt: ' + question_user_answer_attempt)
  localhost_print_function('- - -')
  answer_is_correct = False


  # ------------------------ Check If Answer Is Year Only START ------------------------
  if len(question_admin_correct_answer) == 4:
    try:
      question_admin_correct_answer = int(question_admin_correct_answer)
      # If this ^ try goes through, then at this point you know that the answer must be a YYYY format. If it is not then return false within this check, do not let it go onto other checks.
      if len(question_user_answer_attempt) == 4:
        try:
          question_user_answer_attempt = int(question_user_answer_attempt)
          if question_admin_correct_answer == question_user_answer_attempt:
            localhost_print_function('- - - - - - - - -')
            localhost_print_function('CORRECT ANSWER!')
            localhost_print_function('- - - - - - - - -')
            answer_is_correct = True
            localhost_print_function('=========================================== check_user_answer_vs_admin_answer_function END ===========================================')
            return answer_is_correct
          else:
            answer_is_correct = False
            localhost_print_function('=========================================== check_user_answer_vs_admin_answer_function END ===========================================')
            return answer_is_correct
        except:
          answer_is_correct = False
          localhost_print_function('=========================================== check_user_answer_vs_admin_answer_function END ===========================================')
          return answer_is_correct
      else:
        answer_is_correct = False
        localhost_print_function('=========================================== check_user_answer_vs_admin_answer_function END ===========================================')
        return answer_is_correct
    except:
      pass
  # ------------------------ Check If Answer Is Year Only END ------------------------


  # ------------------------ Check Answer Similarity Score START ------------------------
  try:
    answer_match_score = difflib.SequenceMatcher(None, question_admin_correct_answer, question_user_answer_attempt).ratio()*100
    localhost_print_function('- - - - - - - - - - - -')
    localhost_print_function('answer_match_score')
    localhost_print_function(answer_match_score)
    localhost_print_function('- - - - - - - - - - - -')
    if answer_match_score > 80:
      localhost_print_function('- - - - - - - - -')
      localhost_print_function('CORRECT ANSWER!')
      localhost_print_function('- - - - - - - - -')
      answer_is_correct = True
      localhost_print_function('=========================================== check_user_answer_vs_admin_answer_function END ===========================================')
      return answer_is_correct
  except:
    pass
  # ------------------------ Check Answer Similarity Score END ------------------------


  answer_is_correct = False
  localhost_print_function('=========================================== check_user_answer_vs_admin_answer_function END ===========================================')
  return answer_is_correct