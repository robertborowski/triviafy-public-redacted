from flask import redirect
from backend.utils.create_question_page_utils.allowed_image_filesize import allowed_image_filesize_function
import os
from backend.utils.create_question_page_utils.allowed_images import allowed_images_function
# from werkzeug.utils import secure_filename
from backend.utils.aws.create_question_upload_image_aws_s3 import create_question_upload_image_aws_s3_function

def user_upload_image_checks_aws_s3_function(image, file_size):
  print('=========================================== Check user image file upload START ===========================================')
  # Set the parameters for accepting image upload
  allowed_image_extensions_arr = ["JPEG", "JPG", "PNG", "GIF"]
  max_image_filesize_value = 50 * 1024 * 1024

  # Ensuring the filesize is allowed
  if not allowed_image_filesize_function(file_size, max_image_filesize_value):
    print("Filesize exceeded maximum limit (50 MB)")
    print('=========================================== Check user image file upload END ===========================================')
    return redirect('/create/question', code=302)

  # Ensuring the file has a name
  if image.filename == "":
    print("No filename")
    print('=========================================== Check user image file upload END ===========================================')
    return redirect('/create/question', code=302)

  # Ensuring the file type is allowed
  if allowed_images_function(image.filename, allowed_image_extensions_arr):
    # werkzeug.secure_filename not working when uploading to AWS
    # filename = secure_filename(image.filename)

    # Put the image object in aws s3
    aws_upload = create_question_upload_image_aws_s3_function(image)
    print('=========================================== Check user image file upload END ===========================================')
    return True
  
  else:
    print("That file extension is not allowed")
    print('=========================================== Check user image file upload END ===========================================')
    return redirect('/create/question', code=302)