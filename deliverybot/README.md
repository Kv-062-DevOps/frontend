____
Guide for using Deliverybot Chart, Application and using GitHub Helm Actions.
____
# 1. Install Deliverybot App;
* https://github.com/apps/deliverybot
After push(1) or pull request(2) you action will deploy staging(1) or rewiew(2) deployment
# 2. Manage your Deploy;
* https://app.deliverybot.dev/
By this link you can manage your deployment
# 3. For installing manually and had all needed dependencies you can start it with specific values
* Example of such command:
``` helm install production-front charts/front/ --set env[0].name=ENVIRONMENT --set env[0].value=production --set app.name=production-front --set app.version='1' ```

application
===========
Kubernetes application service

Current chart version is `0.0.2`


## Chart Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Kubernetes affinity resource. |
| app.name | string | `"nginx"` | Application name: Can be consistent between tracks. (required) |
| app.version | string | `"v1"` | Application version: Unique tag for this release. (required) |
| env | list | `[]` | Environment variables for the application. |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"nginx"` | Docker image repository. |
| image.tag | string | `"latest"` | Docker image tag. |
| imagePullSecrets | list | `[]` | Defines secrets to use for pulling docker images. |
| ingress.annotations | object | `{}` | Configures annotations for the ingress. |
| ingress.enabled | bool | `false` | Enable ingress resource. |
| ingress.hosts[0].host | string | `"chart-example.local"` | Host name for routing traffic. |
| ingress.hosts[0].paths | list | `["/"]` | Array of routable paths. |
| ingress.tls | list | `[]` | Kubernetes ingress tls resource. |
| livenessProbe | object | `{"httpGet":{"path":"/","port":"http"}}` | Customize the livenessProbe. |
| migrate.command | string | `"rails db:migrate"` | Command to run on the migrate pod. |
| migrate.enabled | bool | `false` | Run a pod before the application is released to migrate. |
| nodeSelector | object | `{}` | Kubernetes node selectors for Deployment resources. |
| readinessProbe | object | `{"httpGet":{"path":"/","port":"http"}}` | Customize the readiness probe. |
| replicaCount | int | `1` | Replica count for deployments. |
| resources | object | `{}` | Kubernetes resources for Deployment resources. |
| secret | string | `nil` | If defined will pull all secrets from this resource using envFrom. |
| service.enabled | bool | `true` | Enable service resource. |
| service.internalPort | int | `80` | Deployment internal port. |
| service.port | int | `80` | Kubernetes service port. |
| service.type | string | `"ClusterIP"` | Kubernetes service type. |
| tolerations | list | `[]` | Kubernetes tolerations for Deployment resources. |
| workers | list | `[]` | Deploy background jobs with the same config as the main app. |
