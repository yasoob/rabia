from django.contrib import admin
from generic.models import HomePage, HomePageImage


# admin.py
class HomePageImageInline(admin.TabularInline):
    model = HomePageImage
    extra = 3
    list_display = ['image_tag', 'imageLink']
    readonly_fields = ['imageLink','image_tag']

class HomePageAdmin(admin.ModelAdmin):
    inlines = [HomePageImageInline]

admin.site.register(HomePage, HomePageAdmin)
#admin.site.register(HomePageImage)
