DATE=$(date +%Y-%m-%d-%H%M%S)

BACKUP_DIR="/Users/tair/Documents/Колледж/Python/VS/Trading_platform/Web_site/WEB/Web_Site/backup"
DB_BACKUP_PATH="$BACKUP_DIR/db"
FILES_BACKUP_PATH="$BACKUP_DIR/files"

DB_NAME="Trading_platform"
DB_USER="postgres"
DB_PASSWORD="7946"

mkdir -p $DB_BACKUP_PATH
mkdir -p $FILES_BACKUP_PATH

PGPASSWORD=$DB_PASSWORD pg_dump -U $DB_USER $DB_NAME > "$DB_BACKUP_PATH/db_backup_$DATE.sql"

tar czf "$FILES_BACKUP_PATH/files_backup_$DATE.tar.gz" /Users/tair/Documents/Колледж/Python/VS/Trading_platform/Web_site/WEB/Web_Site

echo "Backup completed on $DATE"
