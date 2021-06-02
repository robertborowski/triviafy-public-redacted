# ------------------------ Imports START ------------------------
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_if_slack_user_combo_already_exists import select_if_slack_user_combo_already_exists_function
from backend.utils.slack.user_info_data_manipulation.guess_first_last_name import guess_first_last_name_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.uuid_and_timestamp.create_timestamp import create_timestamp_function
from backend.db.queries.insert_queries.insert_triviafy_slack_user_login_information_table import insert_triviafy_user_login_information_table_slack_function
from backend.db.queries.select_queries.select_check_assign_payment_admin import select_check_assign_payment_admin_function
from backend.utils.slack.user_info_data_manipulation.transpose_slack_user_data_to_nested_dict import transpose_slack_user_data_to_nested_dict_function
from backend.utils.quiz_settings_page_utils.setup_company_default_quiz_settings import setup_company_default_quiz_settings_function
# ------------------------ Imports END ------------------------


def update_db_new_user_store_obj_redis_cookie_function(client, authed_response_obj):
  """Check if user is already in database. If not add user to db. Then return user dict"""
  print('=========================================== update_db_new_user_store_obj_redis_cookie_function START ===========================================')
  
  # Get bare minimum info to check if user already exists in database table
  slack_authed_user_id = authed_response_obj['authed_user']['id']
  slack_authed_team_id = authed_response_obj['team']['id']
  slack_authed_channel_id = authed_response_obj['incoming_webhook']['channel_id']

  # Connect to Postgres database
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()
  # Check if user combo already exists in slack db table
  check_slack_user_combo_already_exists_arr = select_if_slack_user_combo_already_exists_function(postgres_connection, postgres_cursor, slack_authed_user_id, slack_authed_team_id, slack_authed_channel_id)

  
  # ------------------------ Account Does Not Exist START ------------------------
  if check_slack_user_combo_already_exists_arr == 'Account Does Not Exist':
    
    # ------------------------ Get User Basic Info START ------------------------
    # Get nessesary variables from the authed response Slack obj for database check/insert
    slack_authed_team_name = authed_response_obj['team']['name']
    slack_authed_channel_name = authed_response_obj['incoming_webhook']['channel']
    slack_authed_bot_user_id = authed_response_obj['bot_user_id']
    slack_authed_token_type = authed_response_obj['token_type']
    slack_authed_access_token = authed_response_obj['access_token']

    try:
      # Authed user, get user information object, slack method
      user_information_obj = client.users_info(
        user = slack_authed_user_id
      )
      # Get additional user information for the database check/insert
      slack_authed_user_name = user_information_obj['user']['name']
      slack_authed_user_real_full_name = user_information_obj['user']['real_name']
      slack_authed_user_email = user_information_obj['user']['profile']['email']
    except:
      slack_authed_user_name = 'unavailable'
      slack_authed_user_real_full_name = 'unavailable'
      slack_authed_user_email = 'unavailable'
    
    try:
      # From the slack full name provided try to guess the first last name
      slack_guess_first_name, slack_guess_last_name = guess_first_last_name_function(slack_authed_user_real_full_name, slack_authed_user_name)
    except:
      slack_guess_first_name = 'unavailable'
      slack_guess_last_name = 'unavailable'
    
    try:
      slack_authed_user_timezone = user_information_obj['user']['tz']
      slack_authed_user_timezone_label = user_information_obj['user']['tz_label']
      slack_authed_user_timezone_offset = user_information_obj['user']['tz_offset']
    except:
      slack_authed_user_timezone = 'unavailable'
      slack_authed_user_timezone_label = 'unavailable'
      slack_authed_user_timezone_offset = -14400
    
    try:
      slack_authed_user_job_title = user_information_obj['user']['profile']['title']
    except:
      slack_authed_user_job_title = 'unavailable'
    # ------------------------ Get User Basic Info END ------------------------


    # ------------------------ Once New User Created START ------------------------
    # If this is the first user on this team_id + channel_id combination then they will be asigned role of payment_admin (payment manager) but this can changed within website once logged in
    first_user_payment_admin = False
    check_if_team_id_channel_id_combo_contains_payment_admin = select_check_assign_payment_admin_function(postgres_connection, postgres_cursor, slack_authed_team_id, slack_authed_channel_id)
    if check_if_team_id_channel_id_combo_contains_payment_admin == 'No team_id + channel_id payment_admin yet':
      
      # ------------------------ Make Person Payment Admin START ------------------------
      first_user_payment_admin = True
      # ------------------------ Make Person Payment Admin END ------------------------
      
      # ------------------------ Create Default Quiz Settings for new Slack team/channel ID-combo START ------------------------
      new_quiz_settings_row_created = setup_company_default_quiz_settings_function(slack_authed_team_id, slack_authed_channel_id)
      print(new_quiz_settings_row_created)
      # ------------------------ Create Default Quiz Settings for new Slack team/channel ID-combo END ------------------------
    # ------------------------ Once New User Created END ------------------------


    # Create uuid and timestamp for insert
    slack_db_uuid = create_uuid_function('user-slack_')
    slack_db_timestamp_created = create_timestamp_function()


    # ------------------------ Insert New User to DB START ------------------------
    # Insert into database
    db_insert_output_message = insert_triviafy_user_login_information_table_slack_function(postgres_connection, postgres_cursor, slack_db_uuid, slack_db_timestamp_created, slack_guess_first_name, slack_guess_last_name, slack_authed_user_real_full_name, slack_authed_user_email, slack_authed_user_id, slack_authed_team_id, slack_authed_team_name, slack_authed_channel_id, slack_authed_channel_name, slack_authed_bot_user_id, first_user_payment_admin, slack_authed_token_type, slack_authed_access_token, slack_authed_user_timezone, slack_authed_user_timezone_label, slack_authed_user_timezone_offset, slack_authed_user_job_title)
    print('user info stored in postgres database')
    # ------------------------ Insert New User to DB END ------------------------


    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)

    # Transpose user data to nested dictionary
    company_name = slack_authed_team_name  
  # ------------------------ Account Does Not Exist END ------------------------  


  # ------------------------ Account Already Exist START ------------------------
  elif check_slack_user_combo_already_exists_arr != 'Account Does Not Exist':
    print('user info was already stored in postgres database')
    # Pull the user info from DB
    slack_db_uuid = check_slack_user_combo_already_exists_arr[0]
    slack_db_timestamp_created = check_slack_user_combo_already_exists_arr[1]
    slack_guess_first_name = check_slack_user_combo_already_exists_arr[2]
    slack_guess_last_name = check_slack_user_combo_already_exists_arr[3]
    slack_authed_user_real_full_name = check_slack_user_combo_already_exists_arr[4]
    slack_authed_user_email = check_slack_user_combo_already_exists_arr[6]
    slack_authed_user_id = check_slack_user_combo_already_exists_arr[7]
    slack_authed_team_id = check_slack_user_combo_already_exists_arr[8]
    slack_authed_team_name = check_slack_user_combo_already_exists_arr[9]
    slack_authed_channel_id = check_slack_user_combo_already_exists_arr[10]
    slack_authed_channel_name = check_slack_user_combo_already_exists_arr[11]
    company_name = check_slack_user_combo_already_exists_arr[12]
    slack_authed_bot_user_id = check_slack_user_combo_already_exists_arr[13]
    first_user_payment_admin = check_slack_user_combo_already_exists_arr[14]
    slack_authed_token_type = check_slack_user_combo_already_exists_arr[15]
    slack_authed_access_token = check_slack_user_combo_already_exists_arr[16]
    slack_authed_user_timezone = check_slack_user_combo_already_exists_arr[17]
    slack_authed_user_timezone_label = check_slack_user_combo_already_exists_arr[18]
    slack_authed_user_timezone_offset = check_slack_user_combo_already_exists_arr[19]
    slack_authed_user_job_title = check_slack_user_combo_already_exists_arr[20]
  # ------------------------ Account Already Exist END ------------------------  


  # ------------------------ Transpose the SQL pulled table to dict START ------------------------
  # Transpose user data to nested dictionary. Make timestamp a string because you cannot upload timestamp to redis as a json obj
  user_nested_dict = transpose_slack_user_data_to_nested_dict_function(slack_db_uuid, str(slack_db_timestamp_created), slack_guess_first_name, slack_guess_last_name, slack_authed_user_real_full_name, slack_authed_user_email, slack_authed_user_id, slack_authed_team_id, slack_authed_team_name, slack_authed_channel_id, slack_authed_channel_name, company_name, slack_authed_bot_user_id, first_user_payment_admin,  slack_authed_token_type, slack_authed_access_token, slack_authed_user_timezone, slack_authed_user_timezone_label, slack_authed_user_timezone_offset, slack_authed_user_job_title)
  # ------------------------ Transpose the SQL pulled table to dict END ------------------------


  # Close postgres db connection
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)

  print('=========================================== update_db_new_user_store_obj_redis_cookie_function END ===========================================')
  return user_nested_dict