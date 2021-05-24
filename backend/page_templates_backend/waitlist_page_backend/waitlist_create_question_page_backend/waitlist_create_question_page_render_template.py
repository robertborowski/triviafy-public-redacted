# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function

# -------------------------------------------------------------- App Setup
waitlist_create_question_page_render_template = Blueprint("waitlist_create_question_page_render_template", __name__, static_folder="static", template_folder="templates")
@waitlist_create_question_page_render_template.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=301)

# -------------------------------------------------------------- App
@waitlist_create_question_page_render_template.route("/create/question/waitlist", methods=['GET','POST'])
def waitlist_create_question_page_render_template_function():
  """Returns /create/question/waitlist page"""
  print('=========================================== /create/question/waitlist Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  # ------------------------ Check if user is signed in START ------------------------
  try:
    user_nested_dict = check_if_user_login_through_cookies_function()
    user_email = user_nested_dict['user_email']
  except:
    print('No account associated with this user')
    print('=========================================== /create/question/waitlist Page END ===========================================')
    return redirect('/', code=301)
  # ------------------------ Check if user is signed in END ------------------------

  
  print('=========================================== /create/question/waitlist Page END ===========================================')
  return render_template('waitlist_page_templates/waitlist_create_question_page_template/index.html',
                          css_cache_busting = cache_busting_output,
                          user_email_html = user_email)