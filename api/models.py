import uuid
from django.db import models
#from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UUIDStorageModel(models.Model):
    """Creates database model to store randomly created UUIDs"""

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    created_datetime = models.DateTimeField( auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)