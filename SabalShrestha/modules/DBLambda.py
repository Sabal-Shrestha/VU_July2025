import os
import boto3
import uuid

def lambda_handler(event, context):
    # Print the event for debugging
    print("Received event:", event)

    # Extract SNS notification message
    try:
        message = event['Records'][0]['Sns']['Message']
    except (KeyError, IndexError) as e:
        print(f"Error extracting SNS message: {e}")
        return {'status': 'error', 'reason': 'No SNS message found'}

    # Get DynamoDB table name from environment variable
    table_name = os.environ.get('TABLE_NAME', 'WebHealthTableV2')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    # Write notification to DynamoDB
    item = {
        'id': str(uuid.uuid4()),
        'notification': message
    }
    try:
        table.put_item(Item=item)
        print(f"Successfully wrote to DynamoDB: {item}")
        return {'status': 'success', 'item': item}
    except Exception as e:
        print(f"Error writing to DynamoDB: {e}")
        return {'status': 'error', 'reason': str(e)}