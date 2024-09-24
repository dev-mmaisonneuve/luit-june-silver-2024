import boto3

s3 = boto3.client('s3')

with open("test_text.txt", 'rb') as f:
    s3.put_object(Bucket="mm15-boto3-09232024", Key="test_text.txt", Body=f, ContentType="text/plain")


s3.upload_file('test_text.txt', 'mm15-boto3-09232024', 'test_text_upload', ExtraArgs+{'contentType':'text/plain'})