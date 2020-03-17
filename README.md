# AWS CodePipeline Notification

A simple notification application sending information about your AWS CodePipeline to Slack or MS Teams using an incoming Webhook.

![Webhook Notification Diagramm](/Webhook\ Notification\ Diagramm.png)

**[Currently for any failed state and the approval action only]**

Slack Preview
![Slack Screenshot](/slack-screenshot.png)

MS Teams Preview
![MS Teams Screenshot](/msteams-screenshot.png)

## Installation / Usage

### Lambda Code (Python 3.6)

Cloudwatch Events Rules trigger a Lambda which sends out basic information about the state of your CodePipeline to either Slack or MS Teams in the appropriate Format using an incoming Webhook API

### Cloudformation Template

Includes:

- Lambda basic execution role
- Permission for Cloudwatch Events to invoke Lambda for the corresponding CW Event Rule
- CW Event Rules
- Python Lambda


Create as a new Cloudformation Stack and provide your WebhookUrl. Choose which Messenger format you would like to use (Slack or MS Teams).

Alternatively from the AWS CLI:
```
aws cloudformation create-stack --stack-name MyStackName --template-body file://CF-PipelineNotification.yaml --capabilities CAPABILITY_IAM
```
