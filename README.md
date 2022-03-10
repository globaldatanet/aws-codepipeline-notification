# AWS CodePipeline Notification

A simple notification application sending different status of your AWS CodePipeline to Slack or MS Teams using an incoming Webhook. You will get notified for any failed state and the approval action only (additional states need new CW Event Rules).

Cloudwatch Events Rule trigger a Lambda which sends out information about the state of your CodePipeline to either Slack or MS Teams in the appropriate Format using an incoming Webhook API.

![Webhook Notification Diagramm](/.readme-assets/webhook-notification-graph.png)

---

## Table of contents

- [AWS CodePipeline Notification](#aws-codepipeline-notification)
  - [Table of contents](#table-of-contents)
  - [Preview](#preview)
    - [Slack](#slack)
    - [MS Teams](#ms-teams)
  - [AWS Lambda Function](#aws-lambda-function)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [for contributor](#for-contributor)
  - [IMPORTANT!](#important)
  - [to check specific source](#to-check-specific-source)

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

# for contributor

first step

```
$ yarn
```

compile in the background

```
$ yarn watch

```

## IMPORTANT!

DO NOT EDIT by package.json


## to check specific source

once you build your source.

```
$ yarn build
```

then, execute synth, deploy etc...

```
$ cdk synth --app='./lib/integ.xxxx.default.js'
or
$ cdk deploy --app='./lib/integ.xxxx.default.js'
```

example of codepipeline event for lambda
```
{
    "version": "0",
    "id": "01234567-EXAMPLE",
    "detail-type": "CodePipeline Pipeline Execution State Change",
    "source": "aws.codepipeline",
    "account": "123456789012",
    "time": "2020-01-24T22:03:07Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:codepipeline:us-east-1:123456789012:myPipeline"
    ],
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "execution-trigger": {
            "trigger-type": "StartPipelineExecution",
            "trigger-detail": "arn:aws:sts::123456789012:assumed-role/Admin/my-user"
        },
        "state": "STARTED",
        "stage": "test",
        "action": "Approval",
        "version": 1
    }
}
```