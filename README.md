# Web Health Monitoring Stack (AWS CDK)

## Overview
This project is an AWS CDK-based solution for real-time web health monitoring. It checks the availability and latency of a specified URL every minute, publishes custom metrics to CloudWatch, triggers alarms, sends notifications via SNS, and logs events to DynamoDB. A CloudWatch dashboard provides live visualization of your web health metrics.

### Architecture
```
sequenceDiagram
	participant EventBridge
	participant Lambda
	participant CloudWatch
	participant SNS
	participant DynamoDB
	EventBridge->>Lambda: Scheduled trigger (every minute)
	Lambda->>CloudWatch: Put custom metrics (availability, latency)
	CloudWatch->>SNS: Alarm triggers notification
	SNS->>DynamoDB Lambda: Notification event
	DynamoDB Lambda->>DynamoDB: Store notification
```

## Features
- Automated Web Health Checks (Lambda, every minute)
- Custom CloudWatch Metrics (1-minute period)
- Alarms & Notifications via SNS (email subscription)
- DynamoDB Logging of notifications for audit/history
- CloudWatch Dashboard for live visualization
- Configurable constants for URL, thresholds, and email

## Prerequisites
- AWS account and credentials configured
- Node.js (for CDK CLI)
- Python 3.9+
- AWS CDK v2 installed (`npm install -g aws-cdk`)
- Python dependencies installed (`pip install -r requirements.txt`)

## Setup & Deployment
```bash
# Create and activate a virtual env (macOS/Linux)
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Bootstrap CDK (first time only in an account/region)
cdk bootstrap

# Synthesize and deploy
cdk synth
cdk deploy
```

## Usage
- Monitoring: View metrics/alarms in CloudWatch (namespace from `modules/constants.py`)
- Notifications: SNS sends emails to the configured address
- Database: Notification events are stored in DynamoDB table `WebHealthTableV2`
- Dashboard: CloudWatch dashboard `URLMonitorDashboard` shows key charts

## Customization
- Monitored URL: `constants.URL_TO_MONITOR` in `modules/constants.py`
- Notification Email: Update SNS subscription in `sabal_shrestha/sabal_shrestha_stack.py`
- Metric Period: Metrics and alarms use a 1-minute period; Lambda runs every minute

## Troubleshooting
- ModuleNotFoundError (aws_cdk): Activate venv and install requirements
- Duplicate construct IDs: Ensure each CDK construct ID in the stack is unique
- EventBridge sub-minute schedule: Not supported; minimum is 1 minute
- Costs: High-resolution metrics can increase CloudWatch costs

## FAQ
- Monitor multiple URLs? Extend the Lambda to iterate a list and add dimensions
- SMS alerts? Add an SNS SMS subscription alongside email
- Change thresholds? Edit alarm thresholds in `sabal_shrestha_stack.py`

## License
MIT License

## Contact
For questions or support, contact your maintainer.
