#!/bin/bash

# Get the directory of the current script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Navigate to project root (two levels up from crm/cron_jobs)
cd "$DIR/../.."

# Activate the virtual environment
source venv/bin/activate

# Run Django shell command to delete inactive customers
deleted_count=$(python manage.py shell -c "
from datetime import timedelta
from django.utils import timezone
from crm.models import Customer

cutoff_date = timezone.now() - timedelta(days=365)
to_delete = Customer.objects.filter(order__isnull=True, created_at__lte=cutoff_date)
count = to_delete.count()
to_delete.delete()
print(count)
")

# Log result with timestamp
echo \"\$(date): Deleted \$deleted_count inactive customers\" >> /tmp/customer_cleanup_log.txt
