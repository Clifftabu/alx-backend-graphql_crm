from celery import shared_task

@shared_task
def send_cleanup_report():
    with open("/tmp/customer_cleanup_log.txt", "r") as f:
        lines = f.readlines()[-5:]  # get last 5 entries
    report = "".join(lines)
    print("Sending Cleanup Report:\n", report)
    with open("/tmp/customer_cleanup_report_sent.txt", "a") as f:
        f.write(f"Report Sent:\n{report}\n")
    return "Report Sent"

@shared_task
def notify_admins():
    print("Admins have been notified about the cleanup operation.")
    with open("/tmp/customer_cleanup_notifications.txt", "a") as f:
        f.write("Admins notified about cleanup at completion.\n")
    return "Admins Notified"
