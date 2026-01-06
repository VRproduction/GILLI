from django.contrib import admin
from .models import *

MAX_OBJECTS = 1

class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber

@admin.register(GeneralSettings)
class GeneralSettingsAdmin(admin.ModelAdmin):
    inlines = [PhoneNumberInline, ]
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    
@admin.register(IndexSlider)
class IndexSliderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    
@admin.register(IndexVideo)
class IndexVideoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

class WhyChooseUsPunktInline(admin.TabularInline):
    model = WhyChooseUsPunkt

@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    inlines = [WhyChooseUsPunktInline, ]

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(FAQ)
admin.site.register(Comment)
admin.site.register(Blog)
admin.site.register(Contact)