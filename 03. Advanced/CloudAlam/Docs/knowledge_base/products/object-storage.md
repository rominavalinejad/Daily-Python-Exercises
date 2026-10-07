# CloudeAlam Object Storage

CloudeAlam Object Storage is an S3-compatible object storage service for storing files, backups, images, videos, logs, and application data.

## Features

Object Storage provides:

- S3-compatible API
- Bucket-based storage
- Access control
- Object versioning
- Lifecycle rules
- Public and private objects
- Multipart uploads

## Storage Classes

### Standard

Standard storage is designed for frequently accessed data.

Price:

- €0.02 per GB/month

### Infrequent Access

Infrequent Access is designed for data that is accessed less frequently.

Price:

- €0.012 per GB/month

## Network Transfer

Data uploaded to Object Storage is free.

Data downloaded from Object Storage is charged according to the monthly network transfer rate.

Internal transfers between supported CloudeAlam services in the same region are free.

## Buckets

Customers can create multiple buckets.

Each bucket has a unique name within the CloudeAlam Object Storage namespace.

Buckets can be configured as private or public.

Private buckets require authentication to access objects.

Public buckets allow unauthenticated access to objects.

## Versioning

Object versioning can be enabled for individual buckets.

When versioning is enabled, previous versions of modified or deleted objects are retained.

Customers are responsible for storage costs associated with retained object versions.

## Lifecycle Rules

Lifecycle rules can automatically:

- Delete objects after a specified period
- Move objects to Infrequent Access storage
- Delete old object versions

## Security

Object Storage supports access keys and bucket-level permissions.

Access keys should never be shared publicly or committed to source code repositories.
