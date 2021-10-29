import uuid
from django.db import models
from django.contrib.auth.models import User
from hh.models import Post
from django.utils import timezone

class Transaction(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    amount = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    transactn_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.transactn_id
