import boto3
import os

aws_access_key = os.getenv('AWS_ACCESS_KEY')
aws_secret_key = os.getenv('AWS_SECRET_KEY')
aws_s3_bucket = os.getenv('AWS_S3_BUCKET')

assert aws_access_key
assert aws_secret_key
assert aws_s3_bucket

s3 = boto3.resource('s3', aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key)
my_bucket = s3.Bucket(aws_s3_bucket)

for object_summary in my_bucket.objects.filter(Prefix=""):
    print(object_summary.key)
    my_bucket.download_file(object_summary.key, 'files/'+object_summary.key)
