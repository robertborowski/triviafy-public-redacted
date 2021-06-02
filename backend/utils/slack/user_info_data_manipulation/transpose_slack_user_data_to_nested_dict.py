def transpose_slack_user_data_to_nested_dict_function(slack_db_uuid, slack_db_timestamp_created, slack_guess_first_name, slack_guess_last_name, slack_authed_user_real_full_name, slack_authed_user_email, slack_authed_user_id, slack_authed_team_id, slack_authed_team_name, slack_authed_channel_id, slack_authed_channel_name, company_name, slack_authed_bot_user_id, first_user_payment_admin,  slack_authed_token_type, slack_authed_access_token, slack_authed_user_timezone, slack_authed_user_timezone_label, slack_authed_user_timezone_offset, slack_authed_user_job_title):
  """Pass in variables about logged in user information and return is as a dictionary"""
  print('=========================================== transpose_slack_user_data_to_nested_dict_function START ===========================================')

  user_dict = {
    'user_uuid' : slack_db_uuid,
    'user_account_created_timestamp' : slack_db_timestamp_created,
    'user_first_name' : slack_guess_first_name,
    'user_last_name' : slack_guess_last_name,
    'user_full_name' : slack_authed_user_real_full_name,
    'user_email' : slack_authed_user_email,
    'slack_user_id' : slack_authed_user_id,
    'slack_team_id' : slack_authed_team_id,
    'slack_team_name' : slack_authed_team_name,
    'slack_channel_id' : slack_authed_channel_id,
    'slack_channel_name' : slack_authed_channel_name,
    'user_company_name' : company_name,
    'slack_bot_user_id' : slack_authed_bot_user_id,
    'user_is_payment_admin' : first_user_payment_admin,
    'slack_token_type' : slack_authed_token_type,
    'slack_access_token' : slack_authed_access_token,
    'slack_timezone' : slack_authed_user_timezone,
    'slack_timezone_label' : slack_authed_user_timezone_label,
    'slack_timezone_offset' : slack_authed_user_timezone_offset,
    'slack_user_job_title' : slack_authed_user_job_title
  }

  print('=========================================== transpose_slack_user_data_to_nested_dict_function END ===========================================')
  return user_dict