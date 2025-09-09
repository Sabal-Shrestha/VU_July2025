
import os
import boto3
import uuid
from decimal import Decimal
import constants

def get_latest_metric(metric_name, namespace, url):
    client = boto3.client('cloudwatch')
    response = client.get_metric_data(
        MetricDataQueries=[
            {
                'Id': 'm1',
                'MetricStat': {
                    'Metric': {
                        'Namespace': namespace,
                        'MetricName': metric_name,
                        'Dimensions': [
                            {'Name': 'URL', 'Value': url}
                        ]
                    },
                    'Period': 60,
                    'Stat': 'Average'
                },
                'ReturnData': True
            }
        ],
        StartTime=datetime.utcnow() - timedelta(minutes=10),
        EndTime=datetime.utcnow(),
        ScanBy='TimestampDescending',
        MaxDatapoints=1
    )
    values = response['MetricDataResults'][0]['Values']
    return values[0] if values else None

from datetime import datetime, timedelta

def lambda_handler(event, context):
    namespace = constants.URL_MONITOR_NAMESPACE
    latency_metric = constants.URL_MONITOR_METRIC_NAME_LATENCY
    availability_metric = constants.URL_MONITOR_METRIC_NAME_AVAILABILITY

    items = []
    for url in constants.URLS_TO_MONITOR:
        latency = get_latest_metric(latency_metric, namespace, url)
        availability = get_latest_metric(availability_metric, namespace, url)

        item = {
            'id': str(uuid.uuid4()),
            'url': url
        }
        if latency is not None:
            item['latency'] = Decimal(str(latency))
        if availability is not None:
            item['availability'] = Decimal(str(availability))
        items.append(item)

    table_name = os.environ.get('TABLE_NAME', 'WebHealthTableV2')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    results = []
    for item in items:
        try:
            table.put_item(Item=item)
            print(f"Successfully wrote to DynamoDB: {item}")
            results.append({'status': 'success', 'item': item})
        except Exception as e:
            print(f"Error writing to DynamoDB: {e}")
            results.append({'status': 'error', 'item': item, 'reason': str(e)})
    return results