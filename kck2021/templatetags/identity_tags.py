# <your_app>/templatetags/identity_tags.py
from django import template

register = template.Library()

@register.filter
def has_status(identity_statuses, status_to_check):
    """Checks if the IdentityStatus queryset contains a status equal to the argument."""
    return identity_statuses.filter(status=status_to_check).exists()
