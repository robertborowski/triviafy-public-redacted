# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
import os
from backend.utils.sanitize_page_outputs.sanitize_page_output_company_name import sanitize_page_output_company_name_function
from backend.utils.free_trial_period_utils.check_if_free_trial_period_is_expired_days_left import check_if_free_trial_period_is_expired_days_left_function

# -------------------------------------------------------------- App Setup
create_question_index_page_render_template = Blueprint("create_question_index_page_render_template", __name__, static_folder="static", template_folder="templates")
@create_question_index_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@create_question_index_page_render_template.route("/create/question/user/form", methods=['GET','POST'])
def create_question_index_page_render_template_function():
  print('=========================================== /create/question/user/form Page START ===========================================')
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  try:
    # ------------------------ Page Load User Pre Checks START ------------------------
    # Check if user logged in through cookies
    user_nested_dict = check_if_user_login_through_cookies_function()

    # Check if user free trial is expired
    user_nested_dict = check_if_free_trial_period_is_expired_days_left_function(user_nested_dict)
    if user_nested_dict == None or user_nested_dict == True:
      return redirect('/subscription', code=302)
    # ------------------------ Page Load User Pre Checks END ------------------------

    # Get user information from the nested dict
    user_company_name = user_nested_dict['user_company_name']
    user_company_name = sanitize_page_output_company_name_function(user_company_name)
    user_channel_name = user_nested_dict['slack_channel_name']
    user_email = user_nested_dict['user_email']

  except:
    print('page load except error hit')
    print('=========================================== /create/question/user/form Page END ===========================================')
    return redirect('/logout', code=302)
    # return redirect('/', code=302)
  

  # ------------------------ Check create question accesss START ------------------------
  # Get personal email
  personal_email = os.environ.get('PERSONAL_EMAIL')

  # If user does not have access to create questions then redirect to waitlist page
  if user_email != personal_email:
    print('redirecting to the create question wait list page!')
    print('=========================================== /create/question/user/form Page END ===========================================')
    return redirect('/create/question/user/waitlist', code=302)
  # ------------------------ Check create question accesss END ------------------------

  
  print('=========================================== /create/question/user/form Page END ===========================================')
  return render_template('create_question_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          user_email_to_html = user_email,
                          free_trial_days_left_to_html = user_nested_dict['trial_period_days_left_int'],
                          free_trial_end_date_to_html = user_nested_dict['free_trial_end_date'])