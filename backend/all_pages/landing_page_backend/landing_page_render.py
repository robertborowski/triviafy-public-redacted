from flask import render_template, Blueprint, session, redirect, request
from backend.utils.app_setup_before.check_if_url_www import check_if_url_www_function
from backend.utils.app_setup_before.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.uuid_and_timestamp.create_uuid import create_uuid_function

landing_page_render = Blueprint("landing_page_render", __name__, static_folder="static", template_folder="templates")

@landing_page_render.before_request
def before_request():
  """Returns: The domain should work with both www and non-www domain. But should always redirect to non-www version"""
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=301)

@landing_page_render.route("/")
def landing_page_render_function():
  """Returns: Renders the landing page"""  
  # Need to create a css unique key so that cache busting can be done
  cache_busting_output = create_uuid_function('css_')
  slack_state_uuid = create_uuid_function('slk_')
  session['state_outgoing'] = slack_state_uuid
  print('- - - - - -')
  print('~ Landing Page ~')
  print(session['state_outgoing'])
  print('- - - - - -')
  return render_template('landing_pages/landing_page.html',
                          css_cache_busting = cache_busting_output,
                          slack_state_uuid_html = slack_state_uuid)