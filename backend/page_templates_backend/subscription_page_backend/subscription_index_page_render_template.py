# -------------------------------------------------------------- Imports
from flask import render_template, Blueprint, redirect, request
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function
from backend.utils.cached_login.check_if_user_login_through_cookies import check_if_user_login_through_cookies_function
from backend.utils.sanitize_page_outputs.sanitize_page_output_company_name import sanitize_page_output_company_name_function

# -------------------------------------------------------------- App Setup
subscription_index_page_render_template = Blueprint("subscription_index_page_render_template", __name__, static_folder="static", template_folder="templates")
@subscription_index_page_render_template.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@subscription_index_page_render_template.route("/subscription", methods=['GET','POST'])
def subscription_index_page_render_template_function():
  print('=========================================== /subscription Page START ===========================================')
  
  # ------------------------ CSS support START ------------------------
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  # ------------------------ CSS support END ------------------------


  try:
    # ------------------------ Page Load User Pre Checks START ------------------------
    # Check if user logged in through cookies
    user_nested_dict = check_if_user_login_through_cookies_function()
    # ------------------------ Page Load User Pre Checks END ------------------------

    # ------------------------ Get Variables From User Nested Dict START ------------------------
    user_payment_admin_status = user_nested_dict['user_is_payment_admin']
    user_company_name = user_nested_dict['user_company_name']
    user_company_name = sanitize_page_output_company_name_function(user_company_name)
    user_channel_name = user_nested_dict['slack_channel_name']
    # ------------------------ Get Variables From User Nested Dict END ------------------------

    
    
  except:
    print('page load except error hit')
    print('=========================================== /subscription Page END ===========================================')
    return redirect('/logout', code=302)
    # return redirect('/', code=302)

  
  print('=========================================== /subscription Page END ===========================================')
  return render_template('subscription_page_templates/index.html',
                          css_cache_busting = cache_busting_output,
                          user_company_name_to_html = user_company_name,
                          user_channel_name_to_html = user_channel_name,
                          user_payment_admin_status_html = user_payment_admin_status)