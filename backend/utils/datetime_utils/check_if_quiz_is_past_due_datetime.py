# -------------------------------------------------------------- Imports
from datetime import date, datetime
from backend.utils.datetime_utils.quiz_due_time_convert_dict import quiz_due_time_convert_dict_function

# -------------------------------------------------------------- Main Function
def check_if_quiz_is_past_due_datetime_function(quiz_end_date, quiz_end_time):
  print('=========================================== check_if_quiz_is_past_due_datetime_function START ===========================================')
  
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


  # ------------------------ Print Variables START ------------------------
  print('- - - - - - - - - -')
  print('todays date')
  print(today_date)
  print('-')
  print('quiz_end_date_comparison')
  print(quiz_end_date_comparison)
  print('- - - - -')
  print('current_hour_int')
  print(current_hour_int)
  print('-')
  print('quiz_end_time_comparison_int')
  print(quiz_end_time_comparison_int)
  print('- - - - - - - - - -')
  # ------------------------ Print Variables END ------------------------


  if today_date >= quiz_end_date_comparison and current_hour_int >= quiz_end_time_comparison_int:
    print('quiz is past due')
    print('=========================================== check_if_quiz_is_past_due_datetime_function END ===========================================')
    return True

  print('quiz is not past due yet')
  print('=========================================== check_if_quiz_is_past_due_datetime_function END ===========================================')
  return None