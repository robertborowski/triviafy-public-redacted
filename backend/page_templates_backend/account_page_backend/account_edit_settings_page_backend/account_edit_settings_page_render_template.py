# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_triviafy_user_login_information_table_slack_all_payment_admins import select_triviafy_user_login_information_table_slack_all_payment_admins_function
from backend.db.queries.select_queries.select_triviafy_user_login_information_table_slack_all_non_payment_admins import select_triviafy_user_login_information_table_slack_all_non_payment_admins_function
from backend.db.connection.redis_connect_to_database import redis_connect_to_database_function
from backend.utils.account_page_uuid_mapping_check_utils.account_page_uuid_mapping_check import account_page_uuid_mapping_check_function

# -------------------------------------------------------------- App Setup
account_edit_settings_page_render_template = Blueprint("account_edit_settings_page_render_template", __name__, static_folder="static", template_folder="templates")
@account_edit_settings_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@account_edit_settings_page_render_template.route("/account/edit/settings", methods=['GET','POST'])
def account_edit_settings_page_render_template_function():
  print('=========================================== /account/edit/settings Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------

  try:
    user_nested_dict = check_if_user_login_through_cookies_function()

    # Get user information from the nested dict
    user_company_name = user_nested_dict['user_company_name']
    user_channel_name = user_nested_dict['slack_channel_name']
    user_first_name = user_nested_dict['user_first_name']
    user_last_name = user_nested_dict['user_last_name']
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']

    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()
    # Connect to redis database pool (no need to close)
    redis_connection = redis_connect_to_database_function()


    # ------------------------ Get All User Payment Admins START ------------------------
    # Get all user payment admins from DB for company
    company_all_payment_admins_arr_raw = select_triviafy_user_login_information_table_slack_all_payment_admins_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id)
    
    company_all_payment_admins_arr = []
    for i in company_all_payment_admins_arr_raw:
      # Create Temporary UUID To Present To User On The Account Page
      temp_uuid_user_mapping_variable = account_page_uuid_mapping_check_function(redis_connection, i[1])
      company_all_payment_admins_arr.append((i[0], temp_uuid_user_mapping_variable))
    # ------------------------ Get All User Payment Admins END ------------------------


    # ------------------------ Get All Non User Payment Admins START ------------------------
    # Get all user non payment admins from DB for company
    company_all_non_payment_admins_arr_raw = select_triviafy_user_login_information_table_slack_all_non_payment_admins_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id)
    
    # If all users on team are payment admin
    if company_all_non_payment_admins_arr_raw == None:
      company_all_non_payment_admins_arr = []
    
    else:
      company_all_non_payment_admins_arr = []
      for i in company_all_non_payment_admins_arr_raw:
        # Create Temporary UUID To Present To User On The Account Page
        temp_uuid_user_mapping_variable = account_page_uuid_mapping_check_function(redis_connection, i[1])
        company_all_non_payment_admins_arr.append((i[0], temp_uuid_user_mapping_variable))
    # ------------------------ Get All Non User Payment Admins END ------------------------
  
  
    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)

  except:
    print('=========================================== /account/edit/settings Page END ===========================================')
    return redirect('/', code=302)
  
  print('=========================================== /account/edit/settings Page END ===========================================')
  return render_template('account_page_templates/account_edit_settings_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          user_first_name_to_html = user_first_name,
                          user_last_name_to_html = user_last_name,
                          company_all_payment_admins_arr_to_html = company_all_payment_admins_arr,
                          company_all_non_payment_admins_arr_to_html = company_all_non_payment_admins_arr)