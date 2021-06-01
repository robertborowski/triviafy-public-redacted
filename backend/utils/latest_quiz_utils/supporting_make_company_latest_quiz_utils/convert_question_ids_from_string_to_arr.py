# -------------------------------------------------------------- Imports

# -------------------------------------------------------------- Main Function
def convert_question_ids_from_string_to_arr_function(quiz_question_ids_str):
  """ Convert question ID's from single string to an array """
  print('=========================================== convert_question_ids_from_string_to_arr_function START ===========================================')
  
  # Remove the beginning and ending {}
  quiz_question_ids_str_removed_brackets = quiz_question_ids_str[1:-1]

  # Split the string
  quiz_question_ids_arr = quiz_question_ids_str_removed_brackets.split(',')

  print('returning quiz_question_ids_arr')
  print(quiz_question_ids_arr)
  print('=========================================== convert_question_ids_from_string_to_arr_function END ===========================================')
  return quiz_question_ids_arr