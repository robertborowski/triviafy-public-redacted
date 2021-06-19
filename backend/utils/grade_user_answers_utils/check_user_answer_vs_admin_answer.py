# -------------------------------------------------------------- Imports
import difflib

# -------------------------------------------------------------- Main Function
def check_user_answer_vs_admin_answer_function(question_admin_correct_answer, question_user_answer_attempt):
  print('=========================================== check_user_answer_vs_admin_answer_function START ===========================================')
  
  # ------------------------ Pre Check Sanitize START ------------------------
  question_admin_correct_answer = question_admin_correct_answer.lower()
  question_admin_correct_answer = question_admin_correct_answer.strip()
  question_admin_correct_answer = question_admin_correct_answer.replace(' ','_')
  question_user_answer_attempt = question_user_answer_attempt.lower()
  # ------------------------ Pre Check Sanitize END ------------------------
  
  print('- - - - - - ATTEMPTING TO GRADE  - - - - - - -')
  print('question_admin_correct_answer: ' + question_admin_correct_answer)
  print('question_user_answer_attempt: ' + question_user_answer_attempt)
  print('- - -')
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
            print('- - - - - - - - -')
            print('CORRECT ANSWER!')
            print('- - - - - - - - -')
            answer_is_correct = True
            print('=========================================== check_user_answer_vs_admin_answer_function END ===========================================')
            return answer_is_correct
          else:
            answer_is_correct = False
            print('=========================================== check_user_answer_vs_admin_answer_function END ===========================================')
            return answer_is_correct
        except:
          answer_is_correct = False
          print('=========================================== check_user_answer_vs_admin_answer_function END ===========================================')
          return answer_is_correct
      else:
        answer_is_correct = False
        print('=========================================== check_user_answer_vs_admin_answer_function END ===========================================')
        return answer_is_correct
    except:
      pass
  # ------------------------ Check If Answer Is Year Only END ------------------------


  # ------------------------ Check Answer Similarity Score START ------------------------
  try:
    answer_match_score = difflib.SequenceMatcher(None, question_admin_correct_answer, question_user_answer_attempt).ratio()*100
    print('- - - - - - - - - - - -')
    print('answer_match_score')
    print(answer_match_score)
    print('- - - - - - - - - - - -')
    if answer_match_score > 80:
      print('- - - - - - - - -')
      print('CORRECT ANSWER!')
      print('- - - - - - - - -')
      answer_is_correct = True
      print('=========================================== check_user_answer_vs_admin_answer_function END ===========================================')
      return answer_is_correct
  except:
    pass
  # ------------------------ Check Answer Similarity Score END ------------------------


  answer_is_correct = False
  print('=========================================== check_user_answer_vs_admin_answer_function END ===========================================')
  return answer_is_correct