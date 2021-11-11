# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def insert_user_new_questionnaire_response_function(postgres_connection, postgres_cursor, questionnaire_uuid, questionnaire_timestamp, user_slack_uuid, user_slack_team_id, user_slack_channel_id, user_form_input_hear_about, user_form_input_gain_from, user_form_input_coworker_amount, user_form_input_if_competitor):
  localhost_print_function('=========================================== insert_user_new_questionnaire_response_function START ===========================================')
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_new_user_questionnaire_response_table(questionnaire_uuid,questionnaire_timestamp,questionnaire_user_slack_uuid_fk,questionnaire_user_slack_team_id_fk,questionnaire_user_slack_channel_id_fk,questionnaire_user_hear_about,questionnaire_user_gain_from,questionnaire_user_coworker_amount,questionnaire_user_if_competitor) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (questionnaire_uuid, questionnaire_timestamp, user_slack_uuid, user_slack_team_id, user_slack_channel_id, user_form_input_hear_about, user_form_input_gain_from, user_form_input_coworker_amount, user_form_input_if_competitor)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()
    
    localhost_print_function('=========================================== insert_user_new_questionnaire_response_function END ===========================================')
    return True
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== insert_user_new_questionnaire_response_function END ===========================================')
      return False
  # ------------------------ Insert attempt END ------------------------