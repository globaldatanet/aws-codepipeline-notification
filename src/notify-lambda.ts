import * as path from 'path';
import {
  aws_iam as iam,
  aws_lambda as lambda,
  aws_logs as logs,
  aws_events_targets as targets,
  aws_events as events,
  Duration,
} from 'aws-cdk-lib';
import { Construct } from 'constructs';


export interface Props {
  readonly webhookUrl: string;
  readonly messenger: string;
}

export class PipelineNotification extends Construct {
  constructor(scope: Construct, id: string, props: Props) {
    super(scope, id);
    const {
      webhookUrl,
      messenger,
    } = props;

    const fn = new lambda.Function(this, 'lambda', {
      runtime: lambda.Runtime.PYTHON_3_7,
      code: lambda.Code.fromAsset(
        path.join(__dirname, '../lambda/pipeline-notification'),
      ),
      handler: 'app.handler',
      logRetention: logs.RetentionDays.ONE_MONTH,
      environment: {
        WebhookUrl: webhookUrl,
        Messenger: messenger,
      },
      role: new iam.Role(this, 'Role', {
        assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
        inlinePolicies: {
          LambdaLoggingPolicy: new iam.PolicyDocument({
            statements: [
              new iam.PolicyStatement({
                actions: [
                  'logs:CreateLogGroup',
                  'logs:CreateLogStream',
                  'logs:PutLogEvents',
                ],
                resources: ['*'],
              }),
            ],
          }),
        },
      }),
      timeout: Duration.seconds(300),
    });

    new events.Rule(this, 'rule', {
      enabled: true,
      eventPattern: {
        source: [
          'aws.codepipeline',
        ],
        detail: { state: ['STARTED', 'FAILED'] },
      },
      targets: [new targets.LambdaFunction(fn, {})],
    });
  }
}
