# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function

# -------------------------------------------------------------- App Setup
dashboard_index_page_render_template = Blueprint("dashboard_index_page_render_template", __name__, static_folder="static", template_folder="templates")
@dashboard_index_page_render_template.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@dashboard_index_page_render_template.route("/dashboard", methods=['GET','POST'])
def dashboard_index_page_render_template_function():
  """Returns dashboard page"""
  print('=========================================== /dashboard Page START ===========================================')
  
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

    # Need to write a function to calculate the latest quiz info, in the meantime just assign it
    user_team_latest_quiz_info = ['1', '11/25/21']
  except:
    print('=========================================== /dashboard Page END ===========================================')
    return redirect('/', code=302)
  # ------------------------ Check if user is signed in END ------------------------


  
  print('=========================================== /dashboard Page END ===========================================')
  return render_template('dashboard_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          user_team_latest_quiz_number_to_html = user_team_latest_quiz_info[0],
                          user_team_latest_quiz_due_to_html = user_team_latest_quiz_info[1])