from django.contrib import admin
from .models import workview , LatestWork, OurFavourites, BehindTheScenes, stories_data 
# Register your models here.
admin.site.register(workview)
admin.site.register(LatestWork)
admin.site.register(OurFavourites)
admin.site.register(BehindTheScenes)
admin.site.register(stories_data)
