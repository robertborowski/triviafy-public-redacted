def change_uploaded_image_filename_function(image, create_question_uploaded_image_uuid):
  print('=========================================== change_uploaded_image_filename_function START ===========================================')
  # Get the filename
  filename = image.filename

  # Split the filename by '.'
  filename_parts_arr = filename.split('.')

  # Replace the first part of the filename
  filename_parts_arr[0] = create_question_uploaded_image_uuid

  # Join it back together
  filename = ".".join(filename_parts_arr)

  # Assign to the image filename
  image.filename = filename

  print('=========================================== change_uploaded_image_filename_function END ===========================================')
  return image