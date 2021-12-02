# -------------------------------------------------------------- Imports
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.uuid_and_timestamp.create_timestamp import create_timestamp_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
from backend.db.queries.insert_queries.insert_queries_triviafy_categories_selected_table.insert_category_table import insert_category_table_function
from backend.db.queries.select_queries.select_queries_triviafy_categories_selected_table.select_check_default_categories_exist import select_check_default_categories_exist_function


# -------------------------------------------------------------- Main Function
def check_insert_default_categories_team_channel_combo_function(postgres_connection, postgres_cursor, categories_team_id_fk, categories_channel_id_fk):
  localhost_print_function('=========================================== check_insert_default_categories_team_channel_combo_function START ===========================================')
    
  # Check if team channel combo default categories already exist in DB
  default_categories_already_exist = select_check_default_categories_exist_function(postgres_connection, postgres_cursor, categories_team_id_fk, categories_channel_id_fk)

  # If team channel combo default categories already exist
  if default_categories_already_exist == True:
    pass
  # If team channel combo default categories do not already exist
  else:
    categories_uuid_pk = create_uuid_function('category_uuid_')
    categories_timestamp = create_timestamp_function()
    categories_selected = 'All Categories'
    output_message = insert_category_table_function(postgres_connection, postgres_cursor, categories_uuid_pk, categories_timestamp, categories_team_id_fk, categories_channel_id_fk, categories_selected)

  localhost_print_function('=========================================== check_insert_default_categories_team_channel_combo_function END ===========================================')
  return True