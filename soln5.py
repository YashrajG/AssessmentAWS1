import json
import os
import boto3

def lambda_handler(event, context):
    
    s3 = boto3.resource('s3')
    destinationBucket = s3.Bucket(os.environ['destinationBucket'])
    
    key = event['Records'][0]['s3']['object']['key']
    copy_source = {
    'Bucket': event['Records'][0]['s3']['bucket']['name'],
    'Key': key
    }
    
    obj = destinationBucket.Object(key)
    obj.copy(copy_source)
    
    return {
        'statusCode': 200,
        }

