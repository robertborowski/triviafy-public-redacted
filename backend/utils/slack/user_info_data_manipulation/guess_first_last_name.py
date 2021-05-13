def guess_first_last_name_function(input_string_full_name, input_string_name):
  try:
    arr = input_string_full_name.split(' ')
    guess_first_name = arr[0]
    guess_last_name = arr[1]
    return guess_first_name, guess_last_name
  except:
    guess_first_name = input_string_name
    guess_last_name = 'None'
    return guess_first_name, guess_last_name