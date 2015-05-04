from django.db import models
from django.utils.encoding import smart_unicode
import uuid
# Create your models here.


#attempt 1
class Tweetv2(models.Model):
	id = models.CharField(primary_key=True, max_length=64, default=uuid.uuid1)
	tweet = models.CharField(max_length=255, null=True, blank=True)
	symptom = models.CharField(max_length=255, null=True, blank=True)
	def __unicode__(self):
		return smart_unicode(self.id)
#attempt 2
class Tweetv3(models.Model):
        id = models.CharField(primary_key=True, max_length=64, default=uuid.uuid1)
        tweet = models.CharField(max_length=255, null=True, blank=True)
        drug = models.CharField(max_length=255, null=True, blank=True)
        def __unicode__(self):
                return smart_unicode(self.id)

#attempt 3
class DrugSymptom(models.Model):
	id = models.CharField(primary_key=True, max_length=64, default=uuid.uuid1)
	drug = models.CharField(max_length=255, null=True, blank=True)
	symptom = models.CharField(max_length=255, null=True, blank=True)
	def __unicode__(self):
		return smart_unicode(self.id)
#production
class Drugtweet(models.Model):
	id = models.CharField(primary_key=True, max_length=64, default=uuid.uuid1)
	drug = models.CharField(max_length=255, null=True, blank=True)
	symptom = models.CharField(max_length=255, null=True, blank=True)
	tweet = models.CharField(max_length=255, null=True, blank=True)
	def __unicode__(self):
		return smart_unicode(self.id)


