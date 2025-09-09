import os
import boto3
import uuid
from decimal import Decimal

def lambda_handler(event, context):

    # First try to use previous values from event
    latency = event.get('latency')
    availability = event.get('availability')
    if latency is not None and availability is not None:
        print("Using previously tested values from event, not invoking WebHealthLambda.")
    else:
        print("Previous values not found, invoking WebHealthLambda to get fresh metrics.")
        lambda_client = boto3.client('lambda')
        webhealth_lambda_name = os.environ.get('WEBHEALTH_LAMBDA_NAME', 'WebHealthLambda')
        try:
            response = lambda_client.invoke(
                FunctionName=webhealth_lambda_name,
                InvocationType='RequestResponse',
                Payload=b'{}'
            )
            payload = response['Payload'].read()
            import json
            metrics = json.loads(payload)
            latency = metrics.get('latency')
            availability = metrics.get('availability')
        except Exception as e:
            print(f"Error invoking WebHealthLambda: {e}")
            latency = None
            availability = None

    item = {
        'id': str(uuid.uuid4())
    }
    if latency is not None:
        # Convert float to Decimal for DynamoDB
        item['latency'] = Decimal(str(latency))
    if availability is not None:
        # Convert float/int to Decimal for DynamoDB
        item['availability'] = Decimal(str(availability))

    # Get DynamoDB table name from environment variable
    table_name = os.environ.get('TABLE_NAME', 'WebHealthTableV2')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    # Write latency and availability to DynamoDB
    try:
        table.put_item(Item=item)
        print(f"Successfully wrote to DynamoDB: {item}")
        return {'status': 'success', 'item': item}
    except Exception as e:
        print(f"Error writing to DynamoDB: {e}")
        return {'status': 'error', 'reason': str(e)}