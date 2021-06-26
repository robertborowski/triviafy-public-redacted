# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def quiz_due_time_convert_dict_function():
  localhost_print_function('=========================================== quiz_due_time_convert_dict_function START ===========================================')
  
  quiz_time_convert_dict = {
    '1 AM' : "01:00:00",
    '2 AM' : "02:00:00",
    '3 AM' : "03:00:00",
    '4 AM' : "04:00:00",
    '5 AM' : "05:00:00",
    '6 AM' : "06:00:00",
    '7 AM' : "07:00:00",
    '8 AM' : "08:00:00",
    '9 AM' : "09:00:00",
    '10 AM' : "10:00:00",
    '11 AM' : "11:00:00",
    '12 Noon' : "12:00:00",
    '1 PM' : "13:00:00",
    '2 PM' : "14:00:00",
    '3 PM' : "15:00:00",
    '4 PM' : "16:00:00",
    '5 PM' : "17:00:00",
    '6 PM' : "18:00:00",
    '7 PM' : "19:00:00",
    '8 PM' : "20:00:00",
    '9 PM' : "21:00:00",
    '10 PM' : "22:00:00",
    '11 PM' : "23:00:00",
  }

  localhost_print_function('=========================================== quiz_due_time_convert_dict_function END ===========================================')
  return quiz_time_convert_dict