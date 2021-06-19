def sanitize_quiz_question_user_answer_text_function(user_input):
  print('=========================================== sanitize_quiz_question_user_answer_text_function START ===========================================')

  # Check Character count limits
  if len(user_input) < 1 or len(user_input) > 100:
    print('Answer cannot be blank or over 100 characters')
    return None

  # Split the word into a words arr, by default split function is any whitespace
  user_input_words_arr = user_input.split()


  # Sort through the words array to make sure each word is only letters and numbers, no special characters
  for word in range(len(user_input_words_arr)):
    # Check if word is alphnumeric
    check_is_only_alpha_numeric = user_input_words_arr[word].isalnum()
    if check_is_only_alpha_numeric == False:
      print('Answer is not alpha-numeric')
      return None
    # Make word proper case
    user_input_words_arr[word] = user_input_words_arr[word].lower()
    user_input_words_arr[word] = user_input_words_arr[word].capitalize()


  # Join the array back together but replace the whitespace with something else. To avoid harming your DB with words like drop user --> *becomes* -->  drop_user
  user_input_sanitize_output = "_".join(user_input_words_arr)


  print('=========================================== sanitize_quiz_question_user_answer_text_function END ===========================================')
  return user_input_sanitize_output