# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def guess_first_last_name_function(input_string_full_name, input_string_name):
  localhost_print_function('=========================================== guess_first_last_name_function START ===========================================')

  try:
    arr = input_string_full_name.split(' ')
    guess_first_name = arr[0]
    guess_last_name = arr[1]
    localhost_print_function('=========================================== guess_first_last_name_function END ===========================================')
    return guess_first_name, guess_last_name

  except:
    guess_first_name = input_string_name
    guess_last_name = 'None'
    localhost_print_function('=========================================== guess_first_last_name_function END ===========================================')
    return guess_first_name, guess_last_name