def convert_form_results_to_db_inputs_function(user_form_input_quiz_start_day, user_form_input_quiz_start_time, user_form_input_quiz_end_day, user_form_input_quiz_end_time):
  print('=========================================== convert_form_results_to_db_inputs_function START ===========================================')

  # Set the conversion dicts
  quiz_settings_convert_day_dict = {
    'monday' : 'Monday',
    'tuesday' : 'Tuesday',
    'wednesday' : 'Wednesday'
  }
  quiz_settings_convert_time_dict = {
    'nine_am' : '9 AM',
    'ten_am' : '10 AM',
    'eleven_am' : '11 AM',
    'noon' : '12 Noon',
    'one_pm' : '1 PM',
    'two_pm' : '2 PM',
    'three_pm' : '3 PM',
    'four_pm' : '4 PM',
    'five_pm' : '5 PM',
    'six_pm' : '6 PM',
    'seven_pm' : '7 PM'
  }

  # Map the correct new values
  converted_start_day = quiz_settings_convert_day_dict[user_form_input_quiz_start_day]
  converted_start_time = quiz_settings_convert_time_dict[user_form_input_quiz_start_time]
  converted_end_day = quiz_settings_convert_day_dict[user_form_input_quiz_end_day]
  converted_end_time = quiz_settings_convert_time_dict[user_form_input_quiz_end_time]

  print('=========================================== convert_form_results_to_db_inputs_function END ===========================================')
  # return the results
  return converted_start_day, converted_start_time, converted_end_day, converted_end_time