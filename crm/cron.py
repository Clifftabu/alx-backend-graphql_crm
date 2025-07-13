from datetime import timedelta
from django.utils import timezone
from django_cron import CronJobBase, Schedule
from crm.models import Customer
from datetime import datetime
from gql.transport.requests import RequestsHTTPTransport
from gql import gql, Client

from datetime import datetime

def log_crm_heartbeat():
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{datetime.now()}: CRM Heartbeat OK\n")



class LogCRMHeartbeat(CronJobBase):
    schedule = Schedule(run_every_mins=5)
    code = 'crm.log_crm_heartbeat'



    def log_crm_heartbeat():
    ...


    def do(self):
        with open("/tmp/crm_heartbeat_log.txt", "a") as f:
            f.write(f"{datetime.now()}: CRM Heartbeat OK\n")


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

from gql.transport.requests import RequestsHTTPTransport
from gql import gql, Client

def check_graphql_hello():
    transport = RequestsHTTPTransport(url='http://localhost:8000/graphql/', verify=True, retries=3)
    client = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql("{ hello }")
    response = client.execute(query)
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{datetime.now()}: GraphQL hello response: {response}\n")


def update_low_stock():
    from gql.transport.requests import RequestsHTTPTransport
    from gql import gql, Client

    transport = RequestsHTTPTransport(url='http://localhost:8000/graphql/', verify=True, retries=3)
    client = Client(transport=transport, fetch_schema_from_transport=True)

    mutation = gql("""
    mutation {
        updateLowStockProducts {
            message
        }
    }
    """)
    response = client.execute(mutation)
    with open("/tmp/lowstockupdates_log.txt", "a") as f:
        f.write(f"{datetime.now()}: Low stock update response: {response}\n")
