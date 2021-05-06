from flask import render_template, Blueprint, redirect, request, session
from backend.utils.app_setup_before.check_if_url_www import check_if_url_www_function
from backend.utils.app_setup_before.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function

create_account_page_render = Blueprint("create_account_page_render", __name__, static_folder="static", template_folder="templates")

@create_account_page_render.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=301)

@create_account_page_render.route("/create_account")
def create_account_page_render_function():
  """Returns: Renders the create account page"""
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  
  # Render template
  return render_template('create_account_pages/create_account_page.html', css_cache_busting = cache_busting_output)