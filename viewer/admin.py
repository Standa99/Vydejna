from django.contrib import admin
from django.urls import path

from viewer.models import MainCategory, StoreName, StorePlace, SubCategory, SparePart



admin.site.register(MainCategory)
admin.site.register(StoreName)
admin.site.register(StorePlace)
admin.site.register(SubCategory)
admin.site.register(SparePart)

