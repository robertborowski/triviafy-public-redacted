# -------------------------------------------------------------- Imports
from flask import redirect
from backend.utils.create_question_page_utils.allowed_image_filesize import allowed_image_filesize_function
import os
from backend.utils.create_question_page_utils.allowed_images import allowed_images_function
# from werkzeug.utils import secure_filename
from backend.utils.aws.create_question_upload_image_aws_s3 import create_question_upload_image_aws_s3_function
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def user_upload_image_checks_aws_s3_function(image, file_size):
  localhost_print_function('=========================================== Check user image file upload START ===========================================')
  # Set the parameters for accepting image upload
  allowed_image_extensions_arr = ["JPEG", "JPG", "PNG", "GIF"]
  max_image_filesize_value = 50 * 1024 * 1024

  # Ensuring the filesize is allowed
  if not allowed_image_filesize_function(file_size, max_image_filesize_value):
    localhost_print_function('Filesize exceeded maximum limit (50 MB)')
    localhost_print_function('=========================================== Check user image file upload END ===========================================')
    return redirect('/create/question', code=302)

  # Ensuring the file has a name
  if image.filename == "":
    localhost_print_function('No filename')
    localhost_print_function('=========================================== Check user image file upload END ===========================================')
    return redirect('/create/question', code=302)

  # Ensuring the file type is allowed
  if allowed_images_function(image.filename, allowed_image_extensions_arr):
    # werkzeug.secure_filename not working when uploading to AWS
    # filename = secure_filename(image.filename)

    # Put the image object in aws s3
    aws_upload = create_question_upload_image_aws_s3_function(image)
    localhost_print_function('=========================================== Check user image file upload END ===========================================')
    return True
  
  else:
    localhost_print_function('That file extension is not allowed')
    localhost_print_function('=========================================== Check user image file upload END ===========================================')
    return redirect('/create/question', code=302)