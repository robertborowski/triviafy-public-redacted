from flask import render_template, Blueprint, session, redirect, request

landing_page_render = Blueprint("landing_page_render", __name__, static_folder="static", template_folder="templates")

@landing_page_render.route("/")
def landing_page_render_function():
  """Returns: Renders the landing page"""  
  return render_template('landing_pages/landing_page.html')