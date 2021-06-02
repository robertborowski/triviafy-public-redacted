# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function

# -------------------------------------------------------------- App Setup
account_index_page_render_template = Blueprint("account_index_page_render_template", __name__, static_folder="static", template_folder="templates")
@account_index_page_render_template.before_request
def before_request():
  ""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@account_index_page_render_template.route("/account", methods=['GET','POST'])
def account_index_page_render_template_function():
  """Returns account page"""
  print('=========================================== /account Page START ===========================================')
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')

  try:
    user_nested_dict = check_if_user_login_through_cookies_function()

    # Get user information from the nested dict
    user_company_name = user_nested_dict['user_company_name']
    user_channel_name = user_nested_dict['slack_channel_name']

  except:
    print('=========================================== /account Page END ===========================================')
    return redirect('/', code=302)
  
  print('=========================================== /account Page END ===========================================')
  return render_template('account_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name)