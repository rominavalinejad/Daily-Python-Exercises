# CloudeAlam Backup Policy

CloudeAlam provides automated backup options for supported services.

## VPS Backups

VPS automated backups are optional.

When enabled, a VPS is backed up once every 6 hours.

Customers can keep up to 7 daily backup points.

Backup data is stored separately from the primary VPS infrastructure.

## Database Backups

Managed Database instances receive automated backups.

Starter plans retain backups for 7 days.

Standard and Pro plans retain backups for 14 days.

Point-in-time recovery is available for Pro database plans.

## Backup Restoration

Customers can restore a VPS or database from an available backup through the CloudeAlam dashboard.

Restoring a backup may cause service downtime.

Customers should verify restored data before using the restored instance in production.

## Backup Limitations

Backups are not guaranteed to protect against every type of data loss.

Customers are responsible for maintaining additional backups when their business requirements require stronger disaster recovery protection.

Backups should not be considered a replacement for application-level backup strategies.
