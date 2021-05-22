def allowed_image_filesize_function(filesize, max_image_filesize_value):
  if int(filesize) <= max_image_filesize_value:
    return True
  else:
    return False