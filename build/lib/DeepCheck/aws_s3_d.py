import boto3
import os
from botocore.exceptions import NoCredentialsError
from botocore import UNSIGNED
from botocore.config import Config

#constants
bucket_name = "pretrained-baseline-model"

#download_function
def download_from_s3(key_names):
    s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
    bucket_name = "pretrained-baseline-model"

    # Create the 'preprocessing' directory if it doesn't exist
    if not os.path.exists('./pretrained/'):
        os.makedirs('./pretrained/')

    # Get a list of all objects in the bucket
    bucket = s3.Bucket(bucket_name)
    objects = bucket.objects.all()
    for key in key_names:
        file_name = key
        if file_name not in os.listdir('./pretrained'):

            bucket.download_file(file_name, f'./pretrained/{file_name}')
        continue
