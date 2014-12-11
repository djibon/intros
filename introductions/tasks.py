import logging

from django_mailbox.models import Mailbox

from celery.task import periodic_task
from celery.task.schedules import crontab

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@periodic_task(run_every=crontab(minute="*"))
def handle_email():
    mailboxes = Mailbox.active_mailboxes.all()
    
    for mailbox in mailboxes:
        messages = mailbox.get_new_mail()
        for message in message:
            logger.info(
                    'Received %s (from %s)',
                    message.subject,
                    message.from_address
                )
