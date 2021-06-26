# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def sanitize_edit_quiz_setting_time_function(user_input_form):
  localhost_print_function('=========================================== sanitize_edit_quiz_setting_time_function START ===========================================')

  if (user_input_form != 'one_am' and len(user_input_form) != 6) and \
    (user_input_form != 'two_am' and len(user_input_form) != 6) and \
      (user_input_form != 'three_am' and len(user_input_form) != 8) and \
        (user_input_form != 'four_am' and len(user_input_form) != 7) and \
          (user_input_form != 'five_am' and len(user_input_form) != 7) and \
            (user_input_form != 'six_am' and len(user_input_form) != 6) and \
              (user_input_form != 'seven_am' and len(user_input_form) != 8) and \
                (user_input_form != 'eight_am' and len(user_input_form) != 8) and \
                  (user_input_form != 'nine_am' and len(user_input_form) != 7) and \
                    (user_input_form != 'ten_am' and len(user_input_form) != 6) and \
                      (user_input_form != 'eleven_am' and len(user_input_form) != 9) and \
                        (user_input_form != 'noon' and len(user_input_form) != 4) and \
                          (user_input_form != 'one_pm' and len(user_input_form) != 6) and \
                            (user_input_form != 'two_pm' and len(user_input_form) != 6) and \
                              (user_input_form != 'three_pm' and len(user_input_form) != 8) and \
                                (user_input_form != 'four_pm' and len(user_input_form) != 7) and \
                                  (user_input_form != 'five_pm' and len(user_input_form) != 7) and \
                                    (user_input_form != 'six_pm' and len(user_input_form) != 6) and \
                                      (user_input_form != 'seven_pm' and len(user_input_form) != 8) and \
                                        (user_input_form != 'eight_pm' and len(user_input_form) != 8) and \
                                          (user_input_form != 'nine_pm' and len(user_input_form) != 7) and \
                                            (user_input_form != 'ten_pm' and len(user_input_form) != 6) and \
                                              (user_input_form != 'eleven_pm' and len(user_input_form) != 9):
    localhost_print_function('=========================================== sanitize_edit_quiz_setting_time_function END ===========================================')
    return None
  
  localhost_print_function('=========================================== sanitize_edit_quiz_setting_time_function END ===========================================')
  return user_input_form