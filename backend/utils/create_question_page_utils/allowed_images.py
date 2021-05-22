def allowed_images_function(filename, allowed_image_extensions_arr):
  # We only want files with a . in the filename
  if not "." in filename:
    return False

  # Split the extension from the filename
  ext = filename.rsplit(".", 1)[1]

  # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
  if ext.upper() in allowed_image_extensions_arr:
    return True
  else:
    return False