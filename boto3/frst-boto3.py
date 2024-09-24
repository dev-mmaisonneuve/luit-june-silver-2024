import boto3

s3 = boto3.clinet('s3')

response = s3.create_bucket(
    Bucket='mm15-boto3-09232024',

)

print(response)