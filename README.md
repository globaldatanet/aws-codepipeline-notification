# AWS CodePipeline Notification

A simple notification application sending different status of your AWS CodePipeline to Slack or MS Teams using an incoming Webhook. You will get notified for any failed state and the approval action only.

Cloudwatch Events Rule trigger a Lambda which sends out basic information about the state of your CodePipeline to either Slack or MS Teams in the appropriate Format using an incoming Webhook API.

![Webhook Notification Diagramm](/.readme-assets/webhook-notification-graph.png)

## Preview
### Slack:
![Slack](/.readme-assets/slack-screenshot.png)

### MS Teams:
![MS Teams](/.readme-assets/msteams-screenshot.png)

## Webhooks

The messages will send via incoming webooks, which need to be configured on Slack or Microsoft Teams

- [Slack](https://api.slack.com/messaging/webhooks)
- [Teams](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)

## Installation

The installation is automated with Infrastructure as Code using CloudFormation. 

The stack includes:

- Lambda basic execution role
- Permission for Cloudwatch Events to invoke Lambda
- CW Event Rules
- Python Lambda

### AWS CLI

Package and upload to S3:
```
aws cloudformation package \
    --template-file  CF-PipelineNotification.yaml\
    --s3-bucket <YourBucketName> \
    --output-template-file packaged-PipelineNotification.yaml
```

Deploy as a Cloudformation stack:
```
aws cloudformation deploy \
    --template-file packaged-PipelineNotification.yaml \
    --stack-name CF-PipelineNotification \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides \
    WebhookUrl=<YourWebhookUrl> \
    Env=<slack/msteams>
```

