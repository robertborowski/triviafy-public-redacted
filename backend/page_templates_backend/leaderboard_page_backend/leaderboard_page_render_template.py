# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.db.connection.postgres_connect_to_database import postgres_connect_to_database_function
from backend.db.connection.postgres_close_connection_to_database import postgres_close_connection_to_database_function
from backend.db.queries.select_queries.select_company_users import select_company_users_function
from backend.db.queries.select_queries.select_total_user_quiz_wins import select_total_user_quiz_wins_function
from backend.db.queries.select_queries.select_total_user_correct_quiz_answers import select_total_user_correct_quiz_answers_function

# -------------------------------------------------------------- App Setup
leaderboard_page_render_template = Blueprint("leaderboard_page_render_template", __name__, static_folder="static", template_folder="templates")
@leaderboard_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@leaderboard_page_render_template.route("/leaderboard", methods=['GET','POST'])
def leaderboard_page_render_template_function():
  print('=========================================== /leaderboard Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  # ------------------------ Check if user is signed in START ------------------------
  try:
    user_nested_dict = check_if_user_login_through_cookies_function()
    
    # Get user information from the nested dict
    user_company_name = user_nested_dict['user_company_name']
    user_channel_name = user_nested_dict['slack_channel_name']
    slack_workspace_team_id = user_nested_dict['slack_team_id']
    slack_channel_id = user_nested_dict['slack_channel_id']


    # ------------------------ Get All Users From Company START ------------------------
    # Connect to Postgres database
    postgres_connection, postgres_cursor = postgres_connect_to_database_function()

    # Get the UUID and Display name of all users at this company/team/channel
    company_users_arr = select_company_users_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id)

    # Master array of dicts for the Leaderboard datatables html
    users_leaderboard_arr_of_dicts = []

    for i in company_users_arr:
      # Create empty dict to store leaderboard results
      users_leaderboard_dict = {}

      # Set variables from arr pull
      user_uuid = i[0]
      user_name = i[1].replace('_',' ')
      # Get total quiz wins for each user
      total_user_wins_arr = select_total_user_quiz_wins_function(postgres_connection, postgres_cursor, user_uuid)
      total_user_wins_int = int(total_user_wins_arr[0])
      # Get total correct answers for each user
      total_user_correct_quiz_answers_arr = select_total_user_correct_quiz_answers_function(postgres_connection, postgres_cursor, user_uuid)
      total_user_correct_quiz_answers_int = int(total_user_correct_quiz_answers_arr[0])

      # Set the dictionary values for user
      users_leaderboard_dict['name'] = user_name
      users_leaderboard_dict['total_user_wins_int'] = total_user_wins_int
      users_leaderboard_dict['total_user_correct_quiz_answers_int'] = total_user_correct_quiz_answers_int

      # Append the dict to a master arr
      users_leaderboard_arr_of_dicts.append(users_leaderboard_dict)
      # ------------------------ Get All Users From Company END ------------------------

    # Close postgres db connection
    postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)


  except:
    print('except error hit')
    print('=========================================== /leaderboard Page END ===========================================')
    return redirect('/', code=302)
  # ------------------------ Check if user is signed in END ------------------------


  
  print('=========================================== /leaderboard Page END ===========================================')
  return render_template('leaderboad_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          users_leaderboard_arr_of_dicts_to_html = users_leaderboard_arr_of_dicts)