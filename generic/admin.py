from django.contrib import admin
from generic.models import HomePage, HomePageImage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _

class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content')}),
        (_('Advanced options'), {
            'classes': ('collapse', ),
            'fields': (
                'registration_required',
                'template_name',
            ),
        }),
    )


class HomePageImageInline(admin.TabularInline):
    model = HomePageImage
    extra = 3
    list_display = ['image_tag', 'imageLink']
    readonly_fields = ['imageLink','image_tag']

class HomePageAdmin(admin.ModelAdmin):
    inlines = [HomePageImageInline]

admin.site.register(HomePage, HomePageAdmin)

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

