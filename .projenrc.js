const {
  awscdk,
} = require('projen');
const project = new awscdk.AwsCdkConstructLibrary({
  name: 'aws-codepipeline-notification',
  author: 'YutaOkoshi', //TODO:
  authorAddress: 'ookoshiyuuta@gmail.com', //TODO:
  cdkVersion: '2.1.0',
  defaultReleaseBranch: 'main',
  name: 'aws-codepipeline-notification-cdk-construct',
  repositoryUrl: 'https://github.com/justincase-jp/aws-codepipeline-notification-cdk-construct.git',

  /* Runtime dependencies of this module. */
  deps: [
    'cdk-constants',
  ],
  // description: undefined,  /* The description is just a string that helps people understand the purpose of the package. */
  // devDeps: [],             /* Build dependencies for this module. */
  // packageName: undefined,  /* The "name" in package.json. */
  common_exclude: [
    'cdk.out',
    'cdk.context.json',
    'yarn-error.log',
    'coverage',
  ],
});
project.synth();