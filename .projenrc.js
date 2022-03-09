const { awscdk } = require('projen');
const project = new awscdk.AwsCdkConstructLibrary({
  author: 'YutaOkoshi',
  authorAddress: 'ookoshiyuuta@gmail.com',
  cdkVersion: '2.1.0',
  defaultReleaseBranch: 'main',
  name: 'aws-codepipeline-notification-cdk-construct',
  repositoryUrl: 'https://github.com/justincase-jp/aws-codepipeline-notification-cdk-construct.git',

  // deps: [],                /* Runtime dependencies of this module. */
  // description: undefined,  /* The description is just a string that helps people understand the purpose of the package. */
  // devDeps: [],             /* Build dependencies for this module. */
  // packageName: undefined,  /* The "name" in package.json. */
});
project.synth();