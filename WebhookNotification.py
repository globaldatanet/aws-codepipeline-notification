import json
import logging
import os
import time
import re
import botocore.vendored.requests as requests

HOOK_URL = os.environ['WebhookUrl']
MESSENGER = os.environ['Messenger']


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # start logging
    #logger.info("Event: " + str(event))

    #message = json.loads(event['Records'][0]['Sns']['Message'])
    #message = json.loads(event)
    message = event
    logger.info("Message: " + str(message))

    # use data from logs
    pipeline = message['detail']['pipeline']
    awsAccountId = message['account']
    awsRegion = message['region']
    eventTime = message['time']
    stage = message['detail']['stage']
    state = message['detail']['state']
    action = message['detail']['action']
    category = message['detail']['type']['category']
    
    # set the color depending on state/category for Approval
    color = "#808080"
    if action == 'Approval':
        color = "#ff9000"
    elif state == 'SUCCEEDED':
        color = "#00ff00"
    elif state == 'STARTED':
        color = "#00bbff"
    elif state == 'FAILED':
        color = "#ff0000"
		
    # data for message cards
    title = pipeline    
    accountString = "Account"
    regionString = "Region"
    timeString = "Event time (UTC)"
    stageString = "Stage"
    stateString = "State"
    actionString = "Action"
    dateString = re.split('T|Z',eventTime)
    dateString = dateString[0]+" "+dateString[1]
    pipelineURL = "https://"+awsRegion+".console.aws.amazon.com/codesuite/codepipeline/pipelines/"+pipeline+"/view?region="+awsRegion
    
    # MS Teams data
    MSTeams = {
        "title": "%s" % title,
        "info": [ { "facts": [{ "name": accountString, "value": awsAccountId }, { "name": regionString, "value": awsRegion }, { "name": timeString, "value": dateString }, { "name": stageString, "value": stage }, { "name": actionString, "value": action }, { "name": stateString, "value": state }], "markdown": 'true' } ],
        "link": [ { "@type": "OpenUri", "name": "Open in AWS", "targets": [ { "os": "default", "uri": pipelineURL } ] } ]
    }

    # Slack data
    Slack = {
        "title": pipeline+" - "+state+" @ "+stage,
        "info": [{ "title": accountString, "value": awsAccountId, "short": 'false' }, { "title": regionString, "value": awsRegion, "short": 'false' }, { "title": timeString, "value": dateString, "short": 'false' }, { "title": actionString, "value": action, "short": 'false' }]
    }
 
    # build Slack message
    if MESSENGER == "slack":
        message_data = {
            "attachments": [{
                "fallback": "Pipeline Status",
                "color": color,
                "author_name": Slack["title"],
                "author_icon": "https://www.awsgeek.com/AWS-History/icons/AWS-CodePipeline.svg",
                "fields": Slack["info"],
                "footer": "globaldatanet",
                "footer_icon": "https://pbs.twimg.com/profile_images/980056498847010816/JZeg2oTx_400x400.jpg",
                "ts": 1584369590, #TimeStamp for last update
                "actions": [ { "type": "button", "text": { "type": "Open in AWS", "text": "Link Button" }, "url": pipelineURL } ]
        }
    ]
}
    # build MS Teams message
    elif MESSENGER == "msteams":
            message_data = {
                "summary": "summary",
                "@type": "MessageCard",
                "@context": "https://schema.org/extensions",
                "themeColor": color,
                "title": MSTeams["title"],
                "sections": MSTeams["info"],
                "potentialAction": MSTeams["link"]
            }
    
    # send message to webhook
    requests.post(HOOK_URL, json.dumps(message_data))