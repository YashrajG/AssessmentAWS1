import boto3
import time


def create_games_table(dynamodb_client):
    try:
        dt_response = dynamodb_client.describe_table(TableName='Games_kaustubh')
        print("Table already exists")
    except dynamodb_client.exceptions.ResourceNotFoundException:
        tags_list = [
            {'Key': "Email", 'Value': "yashraj.gangal@quantiphi.com"},
            {'Key': "Name", 'Value': "Yashraj Gangal"},
            {'Key': "Project", 'Value': "Mumbai_PE"}
        ]
        
        table = dynamodb_client.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'gid',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'gname',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'rating',
                    'AttributeType': 'N'
                },
            ],
            TableName='Games_yashraj',
            KeySchema=[
                {
                    'AttributeName': 'gid',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'gname',
                    'KeyType': 'RANGE'
                },
            ],
            LocalSecondaryIndexes=[
                {
                    'IndexName': 'gid_rating_index',
                    'KeySchema': [
                        {
                            'AttributeName': 'gid',
                            'KeyType': 'HASH'
                        },
                        {
                            'AttributeName': 'rating',
                            'KeyType': 'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'KEYS_ONLY'
                    },
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            },
            Tags=tags_list
        )

        # Wait until the table exists.
        table.meta.client.get_waiter('table_exists').wait(TableName='Games_yashraj')

def add_items(dynamodb_client):
    response1 = dynamodb_client.put_item(
        TableName='Games_yashraj',
        Item={
            'gid': {
                'N': "1",
            },
            'gname': {
                'S': "FIFA19",
            },
            'publisher': {
                'S': "ea",
            },
            'rating': {
                'N': "9",
            },
            'release_date': {
                'S': "2018/12/01",
            },
            'genres': {
                'SS': ['sport', 'multiplayer'],
            }
        }
    )
    response2 = dynamodb.put_item(
        TableName='Games_yashraj',
        Item={
            'gid': {
                'N': "1",
            },
            'gname': {
                'S': "FIFA18",
            },
            'publisher': {
                'S': "ea",
            },
            'rating': {
                'N': "7",
            },
            'release_date': {
                'S': "2017/12/01",
            },
            'genres': {
                'SS': ['sport', 'multiplayer'],
            }
        }
    )
    response3 = dynamodb.put_item(
        TableName='Games_yashraj',
        Item={
            'gid': {
                'N': "2",
            },
            'gname': {
                'S': "CS:GO",
            },
            'publisher': {
                'S': "steam",
            },
            'rating': {
                'N': "9",
            },
            'release_date': {
                'S': "2016/01/01",
            },
            'genres': {
                'SS': ['shooting', 'firstPerson'],
            }
        }
    )
    response4 = dynamodb.put_item(
        TableName='Games_yashraj',
        Item={
            'gid': {
                'N': "2",
            },
            'gname': {
                'S': "CS:CZ",
            },
            'publisher': {
                'S': "steam",
            },
            'rating': {
                'N': "5",
            },
            'release_date': {
                'S': "2015/01/01",
            },
            'genres': {
                'SS': ['shooting', 'firstPerson'],
            }
        }
    )
    print("Added items to table")


if __name__ == '__main__':
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')
    create_games_table(dynamodb)
    add_items(dynamodb)
