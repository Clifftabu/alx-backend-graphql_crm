from datetime import timedelta
from django.utils import timezone
from django_cron import CronJobBase, Schedule
from crm.models import Customer

class CleanInactiveCustomersCronJob(CronJobBase):
    schedule = Schedule(run_every_mins=60*24)  # runs daily
    code = 'crm.clean_inactive_customers_cron'

    def do(self):
        cutoff_date = timezone.now() - timedelta(days=365)
        to_delete = Customer.objects.filter(order__isnull=True, created_at__lte=cutoff_date)
        count = to_delete.count()
        to_delete.delete()
        
        with open("/tmp/customer_cleanup_log.txt", "a") as f:
            f.write(f"{timezone.now()}: Deleted {count} inactive customers\n")
