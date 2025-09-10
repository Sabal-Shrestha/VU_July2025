# Web Health Monitoring Stack (AWS CDK)

## Overview
This project is an AWS CDK-based solution for real-time web health monitoring. It checks the availability and latency of a specified URL every minute, publishes custom metrics to CloudWatch, triggers alarms, sends notifications via SNS, and logs events to DynamoDB. A CloudWatch dashboard provides live visualization of your web health metrics. The solution is designed for extensibility and cost-efficiency, focusing on core monitoring and alerting features.

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
- Custom CloudWatch Metrics (availability, latency)
- Alarms & Notifications via SNS (email and SMS subscription)
- DynamoDB Logging of metrics for audit/history
- CloudWatch Dashboard for live visualization
- Configurable constants for URLs, thresholds, and email/SMS

## Screenshots

Below are the main features of the Web Health Monitoring Stack.

1. **Custom Web Health Checks**
	![WebHealth Lambda Output](<ScreenShots/WebHealthLambda Output.png>)
	![DBLambda Output](<ScreenShots/DBLambda Output.png>)

2. **CloudWatch Metrics Dashboard (availability, latency)**
	![Default Dashboard](<ScreenShots/Default Dashboard.png>)

3. **Alarms & Notifications via SNS (email and SMS subscription)**
	![Alarm Confirmation](<ScreenShots/Alarm Subscription Confirmation Email.png>)
	![Alarm Confirmed](<ScreenShots/Alarm Subscription Confirmed Email.png>)
	![Alarm Metrics Availability](<ScreenShots/Alarm Metrics for Availability.png>)
	![Alarm Metrics Latency](<ScreenShots/Alarm Metrics for Latency.png>)
	![Alarm Popped Latency](<ScreenShots/Alarm popped for Latency.png>)
	![Alarm Popped Availability](<ScreenShots/Alarm Popped for Availability.png>)

4. **DynamoDB Logging of metrics for audit/history**
	![DynamoDB Table 1](<ScreenShots/DynamoDB Table URL 1.png>)
	![DynamoDB Table 2](<ScreenShots/DynamoDB Table URL 2.png>)


## Setup & Deployment
**Note:** 
When you open the project, your workspace will be at "VU_July2025". For all terminal commands (setup, deployment, etc.), make sure your terminal is in the "SabalShrestha" directory:
```bash
cd SabalShrestha
```

# Prerequisites
* AWS account and credentials configured
* Node.js (for CDK CLI)
* Python 3.9+
* AWS CDK v2 installed (`npm install -g aws-cdk`)
* Python dependencies installed (`pip install -r requirements.txt`)

Then run:
```bash
python3 -m venv .venv
source .venv/bin/activate
cdk bootstrap
cdk synth
cdk deploy
```

## Usage
* Monitoring: View metrics/alarms in CloudWatch (namespace from `modules/constants.py`)
* Notifications: SNS sends emails to the configured address
* Database: Notification events are stored in DynamoDB table `WebHealthTableV2`
* Dashboard: CloudWatch dashboard `CloudWatch-Default` shows key charts

## Customization
* Monitored URL: `constants.URLs_TO_MONITOR` in `modules/constants.py`
* Notification Email/SMS: Update SNS subscriptions in `sabal_shrestha/sabal_shrestha_stack.py`
* Alarm thresholds: Edit in `sabal_shrestha_stack.py`
* Metric Period: Metrics and alarms use a 1-minute period; Lambda runs every minute

## Troubleshooting
* ModuleNotFoundError (aws_cdk): Activate venv and install requirements

**Note:** 
Just Always Smile and Seize the Day.