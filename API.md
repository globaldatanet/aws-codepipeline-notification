# API Reference <a name="API Reference" id="api-reference"></a>

## Constructs <a name="Constructs" id="Constructs"></a>

### PipelineNotification <a name="PipelineNotification" id="aws-codepipeline-notification-cdk-construct.PipelineNotification"></a>

#### Initializers <a name="Initializers" id="aws-codepipeline-notification-cdk-construct.PipelineNotification.Initializer"></a>

```typescript
import { PipelineNotification } from 'aws-codepipeline-notification-cdk-construct'

new PipelineNotification(scope: Construct, id: string, props: Props)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#aws-codepipeline-notification-cdk-construct.PipelineNotification.Initializer.parameter.scope">scope</a></code> | <code>constructs.Construct</code> | *No description.* |
| <code><a href="#aws-codepipeline-notification-cdk-construct.PipelineNotification.Initializer.parameter.id">id</a></code> | <code>string</code> | *No description.* |
| <code><a href="#aws-codepipeline-notification-cdk-construct.PipelineNotification.Initializer.parameter.props">props</a></code> | <code><a href="#aws-codepipeline-notification-cdk-construct.Props">Props</a></code> | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="scope" id="aws-codepipeline-notification-cdk-construct.PipelineNotification.Initializer.parameter.scope"></a>

- *Type:* constructs.Construct

---

##### `id`<sup>Required</sup> <a name="id" id="aws-codepipeline-notification-cdk-construct.PipelineNotification.Initializer.parameter.id"></a>

- *Type:* string

---

##### `props`<sup>Required</sup> <a name="props" id="aws-codepipeline-notification-cdk-construct.PipelineNotification.Initializer.parameter.props"></a>

- *Type:* <a href="#aws-codepipeline-notification-cdk-construct.Props">Props</a>

---

#### Methods <a name="Methods" id="Methods"></a>

| **Name** | **Description** |
| --- | --- |
| <code><a href="#aws-codepipeline-notification-cdk-construct.PipelineNotification.toString">toString</a></code> | Returns a string representation of this construct. |

---

##### `toString` <a name="toString" id="aws-codepipeline-notification-cdk-construct.PipelineNotification.toString"></a>

```typescript
public toString(): string
```

Returns a string representation of this construct.

#### Static Functions <a name="Static Functions" id="Static Functions"></a>

| **Name** | **Description** |
| --- | --- |
| <code><a href="#aws-codepipeline-notification-cdk-construct.PipelineNotification.isConstruct">isConstruct</a></code> | Checks if `x` is a construct. |

---

##### ~~`isConstruct`~~ <a name="isConstruct" id="aws-codepipeline-notification-cdk-construct.PipelineNotification.isConstruct"></a>

```typescript
import { PipelineNotification } from 'aws-codepipeline-notification-cdk-construct'

PipelineNotification.isConstruct(x: any)
```

Checks if `x` is a construct.

###### `x`<sup>Required</sup> <a name="x" id="aws-codepipeline-notification-cdk-construct.PipelineNotification.isConstruct.parameter.x"></a>

- *Type:* any

Any object.

---

#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#aws-codepipeline-notification-cdk-construct.PipelineNotification.property.node">node</a></code> | <code>constructs.Node</code> | The tree node. |

---

##### `node`<sup>Required</sup> <a name="node" id="aws-codepipeline-notification-cdk-construct.PipelineNotification.property.node"></a>

```typescript
public readonly node: Node;
```

- *Type:* constructs.Node

The tree node.

---


## Structs <a name="Structs" id="Structs"></a>

### Props <a name="Props" id="aws-codepipeline-notification-cdk-construct.Props"></a>

#### Initializer <a name="Initializer" id="aws-codepipeline-notification-cdk-construct.Props.Initializer"></a>

```typescript
import { Props } from 'aws-codepipeline-notification-cdk-construct'

const props: Props = { ... }
```

#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#aws-codepipeline-notification-cdk-construct.Props.property.messenger">messenger</a></code> | <code>string</code> | *No description.* |
| <code><a href="#aws-codepipeline-notification-cdk-construct.Props.property.webhookUrl">webhookUrl</a></code> | <code>string</code> | *No description.* |

---

##### `messenger`<sup>Required</sup> <a name="messenger" id="aws-codepipeline-notification-cdk-construct.Props.property.messenger"></a>

```typescript
public readonly messenger: string;
```

- *Type:* string

---

##### `webhookUrl`<sup>Required</sup> <a name="webhookUrl" id="aws-codepipeline-notification-cdk-construct.Props.property.webhookUrl"></a>

```typescript
public readonly webhookUrl: string;
```

- *Type:* string

---



