# -------------------------------------------------------------- Imports
from flask import Blueprint, redirect, request, send_file
from backend.utils.page_www_to_non_www.check_if_url_www import check_if_url_www_function
from backend.utils.page_www_to_non_www.remove_www_from_domain import remove_www_from_domain_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- App Setup
download_example_quiz_pdf_redirect = Blueprint("download_example_quiz_pdf_redirect", __name__, static_folder="static", template_folder="templates")
@download_example_quiz_pdf_redirect.before_request
def before_request():
  www_start = check_if_url_www_function(request.url)
  if www_start:
    new_url = remove_www_from_domain_function(request.url)
    return redirect(new_url, code=302)

# -------------------------------------------------------------- App
@download_example_quiz_pdf_redirect.route("/download/example/quiz/pdf", methods=['GET','POST'])
def download_example_quiz_pdf_redirect_function():
  localhost_print_function('=========================================== /download/example/quiz/pdf Page START ===========================================')
  localhost_print_function('=========================================== /download/example/quiz/pdf Page END ===========================================')
  return send_file("static/images/pdfs/triviafy_example_quiz.pdf", as_attachment=True)