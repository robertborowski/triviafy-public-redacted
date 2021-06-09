# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.utils.sanitize_user_inputs.sanitize_account_edit_settings_company_name import sanitize_account_edit_settings_company_name_function

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
    user_channel_name = user_nested_dict['slack_channel_name']
    user_full_name = user_nested_dict['user_full_name']
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']


    # ------------------------ Sanitize Company Name Input START ------------------------
    if request.form.get('user_input_account_settings_company_name') == user_company_name:
      print('- - - - - - - - - - - - - - - - - - - - -')
      print('company name did not change')
      print('- - - - - - - - - - - - - - - - - - - - -')
    else:
      user_input_quiz_settings_edit_company_name = sanitize_account_edit_settings_company_name_function(request.form.get('user_input_account_settings_company_name'))

      print('- - - - - - ')
      print('- - - - - - ')
      print('- - - - - - ')
      print('user_input_quiz_settings_edit_company_name')
      print(user_input_quiz_settings_edit_company_name)
      print(type(user_input_quiz_settings_edit_company_name))
      print('- - - - - - ')
      print('- - - - - - ')
      print('- - - - - - ')
    # ------------------------ Sanitize Company Name Input END ------------------------



    # ------------------------ Get All User Payment Admins START ------------------------
    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()

    

    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
    # ------------------------ Get All User Payment Admins END ------------------------

  except:
    print('=========================================== /account/edit/settings/processing Page END ===========================================')
    return redirect('/', code=302)
  
  print('=========================================== /account/edit/settings/processing Page END ===========================================')
  return redirect('/account', code=302)