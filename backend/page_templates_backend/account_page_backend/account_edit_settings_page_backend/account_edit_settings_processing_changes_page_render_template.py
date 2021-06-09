# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.utils.sanitize_user_inputs.sanitize_account_edit_settings_company_name import sanitize_account_edit_settings_company_name_function
from backend.utils.sanitize_user_inputs.sanitize_account_edit_settings_first_last_name import sanitize_account_edit_settings_first_last_name_function
from backend.db.queries.update_queries.update_account_edit_settings_company_name import update_account_edit_settings_company_name_function
from backend.db.queries.update_queries.update_account_edit_settings_first_name import update_account_edit_settings_first_name_function
from backend.db.queries.update_queries.update_account_edit_settings_last_name import update_account_edit_settings_last_name_function
from backend.db.queries.update_queries.update_account_edit_settings_full_name import update_account_edit_settings_full_name_function

# -------------------------------------------------------------- App Setup
account_edit_settings_processing_changes_page_render_template = Blueprint("account_edit_settings_processing_changes_page_render_template", __name__, static_folder="static", template_folder="templates")
@account_edit_settings_processing_changes_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@account_edit_settings_processing_changes_page_render_template.route("/account/edit/settings/processing", methods=['GET','POST'])
def account_edit_settings_processing_changes_page_render_template_function():
  print('=========================================== /account/edit/settings/processing Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------

  try:
    user_nested_dict = check_if_user_login_through_cookies_function()

    # Get user information from the nested dict
    user_company_name = user_nested_dict['user_company_name']
    user_first_name = user_nested_dict['user_first_name']
    user_last_name = user_nested_dict['user_last_name']
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']
    user_uuid = user_nested_dict['user_uuid']
    user_is_payment_admin = user_nested_dict['user_is_payment_admin']


    # ------------------------ Sanitize/Update Company Name Input START ------------------------
    user_input_quiz_settings_edit_company_name = request.form.get('user_input_account_settings_company_name')
    if user_input_quiz_settings_edit_company_name == user_company_name:
      print('company name did not change')
      pass
    else:
      user_input_quiz_settings_edit_company_name = sanitize_account_edit_settings_company_name_function(request.form.get('user_input_account_settings_company_name'))
      if user_input_quiz_settings_edit_company_name != None:
        # Connect to Postgres database
        postgres_connection, postgres_cursor = postgres_connect_to_database_function()

        # Update the company name
        output_message = update_account_edit_settings_company_name_function(postgres_connection, postgres_cursor, user_input_quiz_settings_edit_company_name, slack_workspace_team_id, slack_channel_id)
        print(output_message)

        # Close postgres db connection
        postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Sanitize/Update Company Name Input END ------------------------


    # ------------------------ Sanitize/Update User First Name Input START ------------------------
    user_input_quiz_settings_edit_first_name = request.form.get('user_input_account_settings_first_name')
    if user_input_quiz_settings_edit_first_name == user_first_name:
      print('user first name did not change')
      pass
    else:
      user_input_quiz_settings_edit_first_name = sanitize_account_edit_settings_first_last_name_function('user_input_account_settings_first_name')
      if user_input_quiz_settings_edit_first_name != None:
        # Connect to Postgres database
        postgres_connection, postgres_cursor = postgres_connect_to_database_function()

        # Update the company name
        output_message = update_account_edit_settings_first_name_function(postgres_connection, postgres_cursor, user_input_quiz_settings_edit_first_name, user_uuid)
        print(output_message)

        # Close postgres db connection
        postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Sanitize/Update User First Name Input END ------------------------


    # ------------------------ Sanitize/Update User Last Name Input START ------------------------
    user_input_quiz_settings_edit_last_name = request.form.get('user_input_account_settings_last_name')
    if user_input_quiz_settings_edit_last_name == user_last_name:
      print('user last name did not change')
      pass
    else:
      user_input_quiz_settings_edit_last_name = sanitize_account_edit_settings_first_last_name_function('user_input_account_settings_last_name')
      if user_input_quiz_settings_edit_last_name != None:
        # Connect to Postgres database
        postgres_connection, postgres_cursor = postgres_connect_to_database_function()

        # Update the company name
        output_message = update_account_edit_settings_last_name_function(postgres_connection, postgres_cursor, user_input_quiz_settings_edit_last_name, user_uuid)
        print(output_message)

        # Close postgres db connection
        postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Sanitize/Update User Last Name Input END ------------------------


    # ------------------------ Update User Full Name in DB START ------------------------
    if user_input_quiz_settings_edit_first_name == user_first_name and user_input_quiz_settings_edit_last_name == user_last_name:
      print('user first and last name did not change')
    else:
      user_input_quiz_settings_edit_full_name = user_input_quiz_settings_edit_first_name + ' ' + user_input_quiz_settings_edit_last_name
      # Connect to Postgres database
      postgres_connection, postgres_cursor = postgres_connect_to_database_function()

      # Update the company name
      output_message = update_account_edit_settings_full_name_function(postgres_connection, postgres_cursor, user_input_quiz_settings_edit_full_name, user_uuid)
      print(output_message)

      # Close postgres db connection
      postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Update User Full Name in DB END ------------------------




    if user_is_payment_admin == True:
      # ------------------------ Edit Total Payment Admin Users - Class payment-admin START ------------------------
      # For payment-admin class
      no_more_users = False
      counter_payment_admin = 1
      while no_more_users == False:
        try:
          payment_admin_arr = request.form.get('payment-admin-' + str(counter_payment_admin))
          
          if payment_admin_arr == None:
            no_more_users = True

          if payment_admin_arr != None:
            counter_payment_admin += 1
            print('- - - - - - - - - - - - - - - - -')
            print(payment_admin_arr)
            print('- - - - - - - - - - - - - - - - -')
        except:
          no_more_users = True
      # ------------------------ Edit Total Payment Admin Users - Class payment-admin END ------------------------
      # ------------------------ Edit Total Payment Admin Users - Class non-payment-admin START ------------------------
      # For non-payment-admin class
      no_more_users = False
      counter_payment_admin = 1
      while no_more_users == False:
        try:
          payment_admin_arr = request.form.get('non-payment-admin-' + str(counter_payment_admin))
          
          if payment_admin_arr == None:
            no_more_users = True

          if payment_admin_arr != None:
            counter_payment_admin += 1
            print('- - - - - - - - - - - - - - - - -')
            print(payment_admin_arr)
            print('- - - - - - - - - - - - - - - - -')
        except:
          no_more_users = True
      # ------------------------ Edit Total Payment Admin Users - Class non-payment-admin END ------------------------


  except:
    print('=========================================== /account/edit/settings/processing Page END ===========================================')
    return redirect('/', code=302)
  
  print('=========================================== /account/edit/settings/processing Page END ===========================================')
  return redirect('/account', code=302)