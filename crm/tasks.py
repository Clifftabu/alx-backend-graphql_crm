from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from crm.models import Customer
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def clean_inactive_customers_task(self):
    try:
        cutoff_date = timezone.now() - timedelta(days=365)
        to_delete = Customer.objects.filter(order__isnull=True, created_at__lte=cutoff_date)
        count = to_delete.count()
        to_delete.delete()
        logger.info(f"{timezone.now()}: Deleted {count} inactive customers")
        with open("/tmp/customer_cleanup_log.txt", "a") as f:
            f.write(f"{timezone.now()}: Deleted {count} inactive customers\n")
    except Exception as e:
        logger.error(f"Error while cleaning inactive customers: {str(e)}")
        raise self.retry(exc=e)
from celery import shared_task
from datetime import datetime

@shared_task
def generate_crm_report():
    with open("/tmp/crmreportlog.txt", "a") as f:
        f.write(f"{datetime.now()}: CRM report generated.\n")
    return "Report generated"


