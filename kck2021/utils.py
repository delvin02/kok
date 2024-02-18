import uuid
from django.urls import reverse
from .models import ReuploadToken
from django.utils import timezone
from datetime import timedelta

def generate_reupload_link(identity_register):
    token = uuid.uuid4().hex  # Generate a unique token
    expires_at = timezone.now() + timedelta(days=1)  # Token expires in 1 day
    ReuploadToken.objects.create(identity_register=identity_register, token=token, expires_at=expires_at)
    
    # Generate the link using the 'reverse' function to get the URL dynamically
    link = f"{reverse('kck:identity_reupload', kwargs={'token': token})}"
    return link
    