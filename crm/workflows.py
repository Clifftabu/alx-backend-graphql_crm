from celery import chain, group, chord
from crm.tasks import clean_inactive_customers_task
from crm.additional_tasks import send_cleanup_report, notify_admins

def run_cleanup_workflow():
    workflow = chain(
        clean_inactive_customers_task.s(),
        send_cleanup_report.s(),
        notify_admins.s()
    )
    workflow.apply_async()

def run_parallel_reports():
    report_group = group(
        send_cleanup_report.s() for _ in range(3)
    )
    report_group.apply_async()

def run_chord_workflow():
    header = group(
        send_cleanup_report.s() for _ in range(2)
    )
    callback = notify_admins.s()
    workflow = chord(header)(callback)
