# AWS CodePipeline Notification

A simple notification application sending different status of your AWS CodePipeline to Slack or MS Teams using an incoming Webhook. You will get notified for any failed state and the approval action only.

Cloudwatch Events Rule trigger a Lambda which sends out basic information about the state of your CodePipeline to either Slack or MS Teams in the appropriate Format using an incoming Webhook API.

## Preview
![Slack](/slack-screenshot.png)

![MS Teams](/msteams-screenshot.png)

## Installation


### Cloudformation

Includes:

- Lambda basic execution role
- Permission for Cloudwatch Events to invoke Lambda
- CW Event Rules
- Python Lambda

Create as a new Cloudformation Stack and provide your WebhookUrl. Choose which Messenger format you would like to use (Slack or MS Teams).

### AWS CLI
```
aws cloudformation create-stack --stack-name MyStackName --template-body file://CF-PipelineNotification.yaml --capabilities CAPABILITY_IAM
```
