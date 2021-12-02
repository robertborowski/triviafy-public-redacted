# # -------------------------------------------------------------- Imports
# from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
# from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
# from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
# from backend.db.queries.select_queries.select_queries_triviafy_user_login_information_table_slack.select_triviafy_user_login_information_table_slack_all_team_channel_combos import select_triviafy_user_login_information_table_slack_all_team_channel_combos_function
# from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
# from backend.utils.uuid_and_timestamp.create_timestamp import create_timestamp_function
# from backend.db.queries.insert_queries.insert_queries_triviafy_categories_selected_table.insert_category_table import insert_category_table_function
# from backend.db.queries.select_queries.select_queries_triviafy_categories_selected_table.select_check_default_categories_exist import select_check_default_categories_exist_function


# # -------------------------------------------------------------- Main Function
# def job_trial_quiz_categories_function():
#   localhost_print_function('=========================================== job_trial_quiz_categories_function START ===========================================')


#   # ------------------------ Connect to Postgres DB START ------------------------
#   postgres_connection, postgres_cursor = postgres_connect_to_database_function()
#   # ------------------------ Connect to Postgres DB END ------------------------


#   all_team_channel_combos_arr = select_triviafy_user_login_information_table_slack_all_team_channel_combos_function(postgres_connection, postgres_cursor)

#   for i in all_team_channel_combos_arr:
#     categories_team_id_fk = i[0]
#     categories_channel_id_fk = i[1]
    
#     # Check if team channel combo default categories already exist in DB
#     default_categories_already_exist = select_check_default_categories_exist_function(postgres_connection, postgres_cursor, categories_team_id_fk, categories_channel_id_fk)

#     # If team channel combo default categories already exist
#     if default_categories_already_exist == True:
#       pass
#     # If team channel combo default categories do not already exist
#     else:
#       categories_uuid_pk = create_uuid_function('category_uuid_')
#       categories_timestamp = create_timestamp_function()
#       categories_selected = 'All Categories'
#       output_message = insert_category_table_function(postgres_connection, postgres_cursor, categories_uuid_pk, categories_timestamp, categories_team_id_fk, categories_channel_id_fk, categories_selected)


#   # ------------------------ Close Postgres DB START ------------------------
#   postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
#   # ------------------------ Close Postgres DB END ------------------------
  
#   localhost_print_function('=========================================== job_trial_quiz_categories_function END ===========================================')
#   return True



# # ---------------------------------------------------------------------------------------------------------------------------- Job to Run The Main Function
# if __name__ == "__main__":
#   job_trial_quiz_categories_function()