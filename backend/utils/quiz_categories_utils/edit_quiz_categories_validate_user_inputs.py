# -------------------------------------------------------------- Imports
from redis.client import pairs_to_dict_typed
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_queries_triviafy_all_questions_table.select_triviafy_all_questions_table_all_unique_categories import select_triviafy_all_questions_table_all_unique_categories_function

# -------------------------------------------------------------- Main Function
def edit_quiz_categories_validate_user_inputs_function(user_form_categories_selected_arr):
  localhost_print_function('=========================================== edit_quiz_categories_validate_user_inputs_function START ===========================================')

  # ------------------------ Connect to Postgres DB START ------------------------
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()
  # ------------------------ Connect to Postgres DB END ------------------------


  # ------------------------ Pull unique categories from SQL DB START ------------------------
  unique_categories_arr_pulled_from_db = select_triviafy_all_questions_table_all_unique_categories_function(postgres_connection, postgres_cursor)
  # ------------------------ Pull unique categories from SQL DB END ------------------------
  
  # ------------------------ Loop Create Arr of Dicts START ------------------------
  # Create temp set
  temp_set_checker = {''}

  for i_unique_categories in unique_categories_arr_pulled_from_db:
    i_unique_categories_zero = i_unique_categories[0]
    i_unique_categories_zero_split_arr = i_unique_categories_zero.split(',')
    if len(i_unique_categories_zero_split_arr) > 1:
      for word in i_unique_categories_zero_split_arr:
        word = word.strip()
        temp_set_checker.add(word.replace(" ", "_").lower())
    else:
      word = i_unique_categories_zero_split_arr[0]
      temp_set_checker.add(word.replace(" ", "_").lower())
  temp_set_checker.remove('')
  # ------------------------ Loop Create Arr of Dicts END ------------------------


  # ------------------------ Close Postgres DB START ------------------------
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
  # ------------------------ Close Postgres DB END ------------------------

  for i in user_form_categories_selected_arr:
    if i in temp_set_checker:
      pass
    if i not in temp_set_checker:
      localhost_print_function('invalid user input')
      localhost_print_function('=========================================== edit_quiz_categories_validate_user_inputs_function END ===========================================')
      return False


  localhost_print_function('=========================================== edit_quiz_categories_validate_user_inputs_function END ===========================================')
  return True