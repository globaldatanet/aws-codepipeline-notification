import json
import logging
import os
import re
import requests


HOOK_URL = os.environ['WebhookUrl']
MESSENGER = os.environ['Messenger']

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    '''
        main handler
    '''

    # start logging
    logger.info(f'Recieved event: {event}')

    # use data from logs
    pipeline = event['detail']['pipeline']
    aws_account_id = event['account']
    aws_region = event['region']
    event_time = event['time']
    stage = event['detail']['stage']
    state = event['detail']['state']
    action = event['detail']['action']
    # category = message['detail']['type']['category']

    # set the color depending on state/category for Approval
    color = '#808080'
    if action == 'Approval':
        color = '#ff9000'
    elif state == 'SUCCEEDED':
        color = '#00ff00'
    elif state == 'STARTED':
        color = '#00bbff'
    elif state == 'FAILED':
        color = '#ff0000'
    else:
        color = '#000000'

    date = re.split('T|Z',event_time)
    date = f'{date[0]} {date[1]}'
    pipeline_url = f'''https://{aws_region}.console.aws.amazon.com/codesuite/
                        codepipeline/pipelines/{pipeline}/view?region={aws_region}'''

    # build Slack message
    if MESSENGER == 'slack':
        message_data = {
            'attachments': [
                {
                    'fallback': 'Pipeline Status',
                    'color': color,
                    'author_name': f'{pipeline} - {state} @ {stage}',
                    'author_icon': 'https://www.awsgeek.com/AWS-History/icons/AWS-CodePipeline.svg',
                    'fields': [
                        { 'title': 'Account', 'value': aws_account_id, 'short': 'false' },
                        { 'title': 'Region', 'value': aws_region, 'short': 'false' },
                        { 'title': 'Event time (UTC)', 'value': date, 'short': 'false' },
                        { 'title': 'Action', 'value': action, 'short': 'false' }
                    ],
                    'footer': 'globaldatanet',
                    'footer_icon': '''https://pbs.twimg.com/profile_images/980056498847010816/
                                        JZeg2oTx_400x400.jpg''',
                    'ts': 1639133471, # TimeStamp for last update
                    'actions': [
                        {
                            'type': 'button', 'text':
                                { 'type': 'Open in AWS', 'text': 'Link Button' },
                            'url': pipeline_url
                        }
                    ]
                }
            ]
        }
    # build MS Teams message
    elif MESSENGER == 'msteams':
        message_data = {
            'summary': 'summary',
            '@type': 'MessageCard',
            '@context': 'https://schema.org/extensions',
            'themeColor': color,
            'title': f'{pipeline}',
            'sections': [
                {
                    'facts': [
                        { 'name': 'Account', 'value': aws_account_id },
                        { 'name': 'Region', 'value': aws_region },
                        { 'name': 'Event time (UTC)', 'value': date },
                        { 'name': 'Stage', 'value': stage },
                        { 'name': 'Action', 'value': action },
                        { 'name': 'State', 'value': state }
                    ],
                    'markdown': 'true'
                }
            ],
            'potentialAction': {
                '@type': 'OpenUri', 'name': 'Open in AWS', 'targets': [
                        { 'os': 'default', 'uri': pipeline_url }
                    ]
            }
        }

    # send message to webhook
    requests.post(HOOK_URL, json.dumps(message_data))
