import boto3

s3 = boto3.client('s3')  # Make sure 'client' is correctly spelled.

response = s3.create_bucket(
    Bucket='mm15-boto3-09232024',
)

print(response)
