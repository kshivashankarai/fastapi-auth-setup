
celery -A src.servers.celery_tasks.c_app worker --loglevel=INFO &

celery -A src.servers.celery_tasks.c_app flower