import json
import sys
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb' ,region_name='us-east-1')
table = dynamodb.Table('table_blogs')
response = table.query(
    KeyConditionExpression=Key('typeblog').eq(1) and Key('timestampp').eq(11656807581)
)

print(response)  

    
