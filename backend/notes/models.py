from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class Note(models.Model):
    title = models.CharField(_('title'), max_length=10000)
    owner = models.ForeignKey(get_user_model(), name=_(
        'owner'), on_delete=models.CASCADE)
    is_important = models.BooleanField(_('important'), default=False)
    is_research = models.BooleanField(_('research'), default=False)
    is_good_idea = models.BooleanField(_('good idea'), default=False)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    last_modified = models.DateTimeField(_('date edited'), blank=True, null=True)
    
