# CloudeAlam Kubernetes

CloudeAlam Kubernetes provides managed Kubernetes clusters for deploying containerized applications.

CloudeAlam manages the Kubernetes control plane while customers manage their workloads and worker nodes.

## Availability

Kubernetes is currently available in:

- Frankfurt Zone 1
- Frankfurt Zone 2

Multi-zone clusters can distribute worker nodes across multiple availability zones.

## Cluster Types

### Development Cluster

Designed for development and testing.

Maximum recommended worker nodes: 5.

### Production Cluster

Designed for production workloads.

Supports multiple worker nodes and multi-zone deployment.

## Control Plane

The Kubernetes control plane is managed by CloudeAlam.

CloudeAlam is responsible for:

- Kubernetes API availability
- Control plane upgrades
- Control plane monitoring
- Control plane security patches

Customers are responsible for:

- Application deployments
- Container images
- Kubernetes workloads
- Application configuration
- Worker node workloads

## Kubernetes Versions

CloudeAlam currently supports:

- Kubernetes 1.30
- Kubernetes 1.31

Only supported Kubernetes versions receive regular security updates.

## Networking

Clusters receive a private network by default.

Public Load Balancers can be created for applications that require internet access.

## Backups

CloudeAlam does not automatically back up application data stored inside Kubernetes volumes unless the Kubernetes Backup service is explicitly enabled.

Customers are responsible for backing up application data when required.

## Scaling

Worker nodes can be added or removed from a cluster through the CloudeAlam dashboard or API.

Horizontal Pod Autoscaling can be configured at the Kubernetes workload level.
