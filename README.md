# AWS CodePipeline Notification

A simple notification application sending different status of your AWS CodePipeline to Slack or MS Teams using an incoming Webhook. You will get notified for any failed state and the approval action only.

Cloudwatch Events Rule trigger a Lambda which sends out basic information about the state of your CodePipeline to either Slack or MS Teams in the appropriate Format using an incoming Webhook API.

## Preview
![Slack](/slack-screenshot.png)

![MS Teams](/msteams-screenshot.png)

## Webhooks

The messages will send via incoming webooks, which need to be configured on Slack or Microsoft Teams

- [Slack](https://api.slack.com/messaging/webhooks)
- [Teams](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)


### Cloudformation


## Installation

The installation is automated with Infrastructure as Code using CloudFormation. 

The stack includes:

- Lambda basic execution role
- Permission for Cloudwatch Events to invoke Lambda
- CW Event Rules
- Python Lambda

### AWS CLI

| Parameter  | Second Header |
| ------------- | ------------- |
| WebhookUrl  | Incoming Webhook Url  |
| Messenger  | slack / msteams  |

```
aws cloudformation create-stack --stack-name MyStackName --template-body file://CF-PipelineNotification.yaml --capabilities CAPABILITY_IAM
```
