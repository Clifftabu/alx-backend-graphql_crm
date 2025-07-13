INSTALLED_APPS = [
    ...
    'django_cron',
    'django_celery_beat',
    'django_crontab',

]

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'  # adjust as needed

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
CRONJOBS = [
    ('0 8 * * *', 'crm.cron.LogCRMHeartbeat'),
     ('0 8 * * *', 'crm.cron.update_low_stock'),
   
]