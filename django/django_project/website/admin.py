from django.contrib import admin
from website.models import Tweetv2, Tweetv3, DrugSymptom, Drugtweet

# Register your models here.
admin.site.register(Tweetv2)
admin.site.register(Tweetv3)
admin.site.register(DrugSymptom)
admin.site.register(Drugtweet)
