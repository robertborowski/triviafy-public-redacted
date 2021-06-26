# -------------------------------------------------------------- Imports
from datetime import date, datetime
from backend.utils.datetime_utils.quiz_due_time_convert_dict import quiz_due_time_convert_dict_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def check_if_quiz_is_past_due_datetime_function(quiz_end_date, quiz_end_time):
  localhost_print_function('=========================================== check_if_quiz_is_past_due_datetime_function START ===========================================')
  
  # ------------------------ Assign Variables START ------------------------
  # Variables for comparing dates
  today_date = date.today()                                                       # date
  quiz_end_date_comparison = datetime.strptime(quiz_end_date, '%Y-%m-%d').date()  # date
  
  # Variables for comparing times
  current_time = datetime.now().strftime("%H:%M:%S")                  # str
  current_hour_int = int(current_time[0:2])                           # int
  quiz_time_convert_dict = quiz_due_time_convert_dict_function()
  quiz_end_time_comparison = quiz_time_convert_dict[quiz_end_time]    # str
  quiz_end_time_comparison_int = int(quiz_end_time_comparison[0:2])   # int
  # ------------------------ Assign Variables END ------------------------
  

  # ------------------------ Checks START ------------------------
  if today_date > quiz_end_date_comparison:
    localhost_print_function('Today is greater than the quiz due date')
    localhost_print_function('=========================================== check_if_quiz_is_past_due_datetime_function END ===========================================')
    return True
  
  elif today_date == quiz_end_date_comparison:
    if current_hour_int >= quiz_end_time_comparison_int:
      localhost_print_function('Today is equal to the quiz due date, and current hour is greater than due date hour')
      localhost_print_function('=========================================== check_if_quiz_is_past_due_datetime_function END ===========================================')
      return True
  # ------------------------ Checks END ------------------------


  localhost_print_function('quiz is not past due yet')
  localhost_print_function('=========================================== check_if_quiz_is_past_due_datetime_function END ===========================================')
  return None