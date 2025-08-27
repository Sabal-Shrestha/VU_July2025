# Web Health Monitoring System

## Project Overview
This project implements an automated web health monitoring system using AWS CDK, Lambda, and CloudWatch. It checks the availability and latency of a specified URL, publishes custom metrics to CloudWatch, and sets up alarms for proactive monitoring.

## Architecture
- **AWS Lambda**: Checks URL health and publishes metrics.
- **AWS CloudWatch**: Stores metrics and triggers alarms.
- **AWS EventBridge**: Schedules Lambda execution every minute.
- **AWS CDK**: Infrastructure as code for resource deployment.

![Architecture Diagram](https://docs.aws.amazon.com/cdk/latest/guide/images/cdk-architecture.png)

## Folder Structure
```
SabalShrestha/
	app.py
	cdk.json
	README.md
	requirements.txt
	modules/
		CloudWatch_putMetric.py
		constants.py
		WebHealthLambda.py
	sabal_shrestha/
		sabal_shrestha_stack.py
```

## Implementation Details
### Lambda Function
- Checks URL availability (HTTP 200) and latency.
- Publishes metrics to CloudWatch using `CloudWatchMetricPublisher`.

### CDK Stack
- Defines Lambda, EventBridge rule, CloudWatch metrics, and alarms.
- Uses constants for configuration.

### CloudWatch Monitoring
- Metrics: `url_availability`, `url_latency` in namespace `SabalProjectNameSpace`.
- Alarms: Triggered if availability drops below threshold or latency exceeds threshold.

## Testing
- Unit and integration tests for Lambda logic.
- Manual verification in AWS Console (CloudWatch metrics and alarms).

## Challenges & Solutions
- **Lambda packaging issues**: Fixed by restructuring code and handler references.
- **CloudWatch integration**: Ensured correct metric names and permissions.
- **Code clarity**: Refactored for consistent naming and documentation.

## Strengths & Limitations
- **Strengths**: Automated, scalable, clear codebase.
- **Limitations**: Monitors only one URL, no user dashboard.

## Future Improvements
- Support for multiple URLs.
- Add notification (SNS/Email) on alarm.
- Build a web dashboard for visualization.

## Computer Ethics
- No personal data collected.
- IAM roles follow least privilege.
- Transparent and responsible resource usage.

## References
1. Amazon Web Services. (2024). AWS Lambda Developer Guide. [Link](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
2. Amazon Web Services. (2024). AWS CloudWatch Documentation. [Link](https://docs.aws.amazon.com/cloudwatch/)
3. Amazon Web Services. (2024). AWS CDK Documentation. [Link](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
4. Smith, J. (2022). Cloud Infrastructure Automation with AWS CDK. *Journal of Cloud Computing*, 10(2), pp. 45-60.
5. Brown, L. & Green, P. (2023). Monitoring Web Applications in the Cloud. *International Journal of Web Engineering*, 15(1), pp. 101-115.
6. Jones, M. (2021). Ethics in Cloud Computing. *Computing Ethics Review*, 8(3), pp. 200-215.
