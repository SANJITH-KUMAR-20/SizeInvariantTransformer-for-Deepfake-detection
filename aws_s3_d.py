import boto3
import os
from botocore.exceptions import NoCredentialsError

def download_from_s3(bucket_name, object_key, local_file_path):
    # Create an S3 client
    s3 = boto3.client('s3')
    if not os.path.exists("./trained_models/"):
        os.mkdir("./trained_models/")

        try:
            # Download the file
            s3.download_file(bucket_name, object_key, local_file_path)
            print(f"Downloaded {object_key} from {bucket_name} to {local_file_path}")
        except NoCredentialsError:
            print("Credentials not available or incorrect.")

# Replace these values with your own
bucket_name = 'your-s3-bucket-name'
object_key = 'path/to/your/file.txt'
local_file_path = 'local/file/path.txt'

download_from_s3(bucket_name, object_key, local_file_path)