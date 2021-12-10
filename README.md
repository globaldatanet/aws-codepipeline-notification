# AWS CodePipeline Notification

A simple notification application sending different status of your AWS CodePipeline to Slack or MS Teams using an incoming Webhook. You will get notified for any failed state and the approval action only (additional states need new CW Event Rules).

Cloudwatch Events Rule trigger a Lambda which sends out information about the state of your CodePipeline to either Slack or MS Teams in the appropriate Format using an incoming Webhook API.

![Webhook Notification Diagramm](/.readme-assets/webhook-notification-graph.png)

---

## Table of contents

1. [Preview](#preview)
    - [Slack](#slack)
    - [MS Teams](#ms-teams)
2. [AWS Lambda Function](#aws-lambda-function)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
    - [AWS CLI](#aws-cli)

---

## Preview

### Slack

![Slack](/.readme-assets/slack-screenshot.png)

### MS Teams

![MS Teams](/.readme-assets/msteams-screenshot.png)

---

## AWS Lambda Function

- **Runtime**: Python 3.8
- **Code**: PipelineNotification.py
- **Environment variables**:

|   KEY     |           VALUE         | SCOPE   |
|-----------|-------------------------|---------|
|WebhookUrl |https://your_webhook_url |Required |
|Messenger  |slack / msteams          |Required |

---

## Prerequisites

The messages will send via incoming webooks, which need to be configured on Slack or Microsoft Teams

- [Slack webhook documentation](https://api.slack.com/messaging/webhooks)
- [Teams webhook documentation](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)

## Installation

The installation is automated with Infrastructure as Code using CloudFormation.

The stack includes:

- Lambda basic execution role
- Permission for Cloudwatch Events to invoke Lambda
- CW Event Rules
- Python Lambda

### AWS CLI

Package and upload to S3:

```bash
aws cloudformation package \
    --template-file  CF-PipelineNotification.yaml\
    --s3-bucket <YourBucketName> \
    --output-template-file packaged-PipelineNotification.yaml
```

Deploy as a Cloudformation stack:

```bash
aws cloudformation deploy \
    --template-file packaged-PipelineNotification.yaml \
    --stack-name CF-PipelineNotification \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides \
        WebhookUrl=<YourWebhookUrl> \
        Env=<slack/msteams>
```
