# CloudeAlam Managed Database

CloudeAlam Managed Database provides managed database instances without requiring customers to maintain the database infrastructure themselves.

CloudeAlam currently supports:

- PostgreSQL
- MySQL
- Redis

## PostgreSQL

PostgreSQL is available in versions:

- PostgreSQL 16
- PostgreSQL 15

The database service includes automated maintenance, monitoring, and backups.

## MySQL

MySQL is available in version:

- MySQL 8.0

MySQL instances include automated maintenance and monitoring.

## Redis

Redis is available in:

- Redis 7

Redis is intended primarily for caching, sessions, queues, and temporary application data.

## Database Plans

### Database Starter

- 2 vCPU
- 4 GB RAM
- 50 GB SSD
- €18/month

Recommended for development environments and small applications.

### Database Standard

- 4 vCPU
- 8 GB RAM
- 150 GB SSD
- €42/month

Recommended for production applications with moderate traffic.

### Database Pro

- 8 vCPU
- 16 GB RAM
- 300 GB SSD
- €85/month

Recommended for larger production workloads.

## Backups

Managed Database instances receive automated daily backups.

Backup retention is 14 days for Standard and Pro plans.

Starter plans have a 7-day backup retention period.

Point-in-time recovery is available for Pro plans.

## High Availability

High Availability is available for Database Pro.

When High Availability is enabled, CloudeAlam maintains a standby database instance.

Automatic failover is supported for PostgreSQL and MySQL.

## Maintenance

Routine maintenance is normally performed during the customer's configured maintenance window.

Customers receive maintenance notifications before planned maintenance.
