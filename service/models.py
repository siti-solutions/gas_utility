# service/models.py
from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    TYPE_CHOICES = [
        ('gas_leak', 'Gas Leak'),
        ('maintenance', 'Maintenance'),
        ('installation', 'Installation'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.request_type}"

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.account_number

# service/models.py
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}"

# service/models.py (update ServiceRequest model's save method)
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=ServiceRequest)
def create_notification(sender, instance, **kwargs):
    if instance.status != 'Pending':
        Notification.objects.create(
            user=instance.user,
            message=f"Your service request {instance.request_type} status has been updated to {instance.status}"
        )

