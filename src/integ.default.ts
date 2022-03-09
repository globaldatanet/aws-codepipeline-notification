
import { App, Stack } from 'aws-cdk-lib';
import { PipelineNotification } from './index';

const app = new App();
const stack = new Stack(app, 'MyStack',
  {
    // env: {
    //   account: auditAccountId,
    //   region: auditRegion,
    // },
  },
);
new PipelineNotification(stack, 'PipelineNotification', {
  webhookUrl: 'xxxxx',
  messenger: 'xxxxx',
});