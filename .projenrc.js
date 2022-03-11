const {
  awscdk,
} = require('projen');

const common_exclude = [
  'cdk.out',
  'cdk.context.json',
  'yarn-error.log',
  'coverage',
];

const project = new awscdk.AwsCdkConstructLibrary({
  name: 'aws-codepipeline-notification-cdk-construct',
  author: 'justincase-jp',
  authorAddress: 'ookoshiyuuta@gmail.com', //TODO:
  cdkVersion: '2.1.0',
  defaultReleaseBranch: 'main',
  repositoryUrl: 'https://github.com/justincase-jp/aws-codepipeline-notification-cdk-construct.git',
  keywords: [
    'codepipeline',
    'notification',
    'notify',
    'slack',
    'teams',
  ],

  /* Runtime dependencies of this module. */
  deps: [
    'cdk-constants',
  ],
  // description: undefined,  /* The description is just a string that helps people understand the purpose of the package. */
  // devDeps: [],             /* Build dependencies for this module. */
  // packageName: undefined,  /* The "name" in package.json. */
  gitignore: [...common_exclude],
});
project.synth();