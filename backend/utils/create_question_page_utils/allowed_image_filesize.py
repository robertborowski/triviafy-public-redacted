def allowed_image_filesize_function(filesize, max_image_filesize_value):
  print('=========================================== allowed_image_filesize_function START ===========================================')
  
  if int(filesize) <= max_image_filesize_value:
    print('=========================================== allowed_image_filesize_function END ===========================================')
    return True
  
  else:
    print('=========================================== allowed_image_filesize_function END ===========================================')
    return False