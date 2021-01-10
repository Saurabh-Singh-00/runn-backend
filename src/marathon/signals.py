from django.db.models import signals
from django.dispatch import receiver
from .models import Runner

@receiver(signals.post_save, sender=Runner)
def save_marathon_by_runner(sender, instance, created, **kwargs):
    print("****************** POST Save ******************")