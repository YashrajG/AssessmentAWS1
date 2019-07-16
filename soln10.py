import boto3
from boto3.dynamodb.conditions import Key


def make_query():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Games_yashraj')
    gid = 2
    query_response = table.query(
        IndexName='gid_rating_index',
        Select='ALL_PROJECTED_ATTRIBUTES',
        KeyConditionExpression=Key('gid').eq(gid)
    )
    for item in query_response['Items']:
        print("gname: {}, rating: {}".format(item['gname'], item['rating']))


if __name__ == '__main__':
    make_query()
