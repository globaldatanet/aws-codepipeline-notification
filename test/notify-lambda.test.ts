import {
  App,
  Stack,
} from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import { PipelineNotification } from '../src';

test('PipelineNotification', () => {
  const app = new App();
  const stack = new Stack(app, 'test-stack');

  const webhookUrl = 'xxxxx';
  const messenger = 'xxxxx';

  new PipelineNotification(stack, 'test', {
    webhookUrl: webhookUrl,
    messenger: messenger,
  });

  const template = Template.fromStack(stack);

  template.resourceCountIs('AWS::Events::Rule', 1);
  template.resourceCountIs('AWS::Lambda::Function', 2);

});
