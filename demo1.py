import boto3
session = boto3.Session()
credentials = session.get_credentials()
s3 = boto3.client('s3')
response = s3.list_buckets()
print(response)
print(credentials.access_key)
print(credentials.secret_key)