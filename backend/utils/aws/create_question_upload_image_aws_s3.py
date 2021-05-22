import boto3
from botocore.exceptions import NoCredentialsError
import os

def create_question_upload_image_aws_s3_function(image_obj):
  """Upload user image to aws s3"""
  print('=========================================== AWS s3 upload to bucket START ===========================================')  
  # Env variables
  aws_s3_bucket = os.environ.get('AWS_TRIVIAFY_BUCKET_NAME')
  aws_s3_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
  aws_s3_key_secret = os.environ.get('AWS_SECRET_ACCESS_KEY')
  
  s3 = boto3.client("s3",
                    aws_access_key_id = aws_s3_key_id,
                    aws_secret_access_key = aws_s3_key_secret)

  # Try the upload to AWS s3 bucket
  try:
    s3.upload_fileobj(image_obj, aws_s3_bucket, image_obj.filename, ExtraArgs={"ContentType": image_obj.content_type})
    print('image stored in aws s3!')
    print('=========================================== AWS s3 upload to bucket END ===========================================')
  except Exception as e:
    # This is a catch all exception, edit this part to fit your needs.
    print("Something Happened: ", e)
    print('=========================================== AWS s3 upload to bucket END ===========================================')
    return e