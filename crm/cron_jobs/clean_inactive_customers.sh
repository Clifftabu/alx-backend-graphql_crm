#!/bin/bash

# Navigate to the Django project root
cd "/mnt/c/Users/cliff/OneDrive - Strathmore University/Documents/ALX Prodev Back End Web Dev Program/Github Repos/alx-backend-graphql_crm"

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
echo "$(date): Deleted $deleted_count inactive customers" >> /tmp/customer_cleanup_log.txt
