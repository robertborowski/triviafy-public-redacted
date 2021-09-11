# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def insert_triviafy_slack_payment_status_table_function(postgres_connection, postgres_cursor, payment_status_uuid, payment_status_timestamp, slack_team_id, slack_channel_id, payment_status_year, payment_status_month, payment_status_day_of_month_due, payment_status_final_paid_customer):
  localhost_print_function('=========================================== insert_triviafy_slack_payment_status_table_function START ===========================================')
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_slack_payment_status_table(payment_status_uuid,payment_status_timestamp,payment_status_slack_team_id,payment_status_slack_channel_id,payment_status_year,payment_status_month,payment_status_day_of_month_due,payment_status_final_paid_customer) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (payment_status_uuid, payment_status_timestamp, slack_team_id, slack_channel_id, payment_status_year, payment_status_month, payment_status_day_of_month_due, payment_status_final_paid_customer)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()

    localhost_print_function('=========================================== insert_triviafy_slack_payment_status_table_function END ===========================================')
    return True
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== insert_triviafy_slack_payment_status_table_function END ===========================================')
      return None
  # ------------------------ Insert attempt END ------------------------