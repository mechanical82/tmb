from django.contrib import admin

from home.models import *
# Register your models here.

class BrieftDraftAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'subtitle')
    list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')


class NatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'crump_title_contact', 'time_create', 'crump_photo_contact', 'is_published')
    list_display_links = ('id', 'crump_title_contact')
    search_fields = ('title', 'crump_subtitle_contact')
    list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_banner', 'time_create', 'photo_banner', 'is_published')
    list_display_links = ('id', 'title_banner')
    search_fields = ('title_banner', 'subtitle_banner')
    list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_block', 'time_create', 'is_published')
    list_display_links = ('id', 'title_block')
    search_fields = ('title_block', 'subtitle_block')
    list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'profession')
    list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')


class DiamondAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    # search_fields = ('title')
    list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')


class ClipdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    # search_fields = ('title')
    list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')


class WeddingringsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    # search_fields = ('title')
    list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')


class EarringAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    # search_fields = ('title')
    list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')


class AmuletsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    # search_fields = ('title')
    list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')


class RingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    # list_editable = ('is_published')


# @admin.register(CallbackRequest)
class CallbackRequestAdmin(admin.ModelAdmin):
    # list_display = ('id', 'email', 'created_at')
    # list_display_links = ('id', 'email')
    # list_editable = ('created_at')
    list_display = ('name', 'phone', 'created_at', 'processed')
    list_filter = ('processed',)
    search_fields = ('name', 'phone')


class BadgeAdmin(admin.ModelAdmin):
    list_display = ('title_banner', 'time_create', 'is_published')
    # list_filter = ('')
    search_fields = ('title_banner', 'subtitle_banner')


class BadgeFotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'time_create')
    # list_filter = ('',)
    search_fields = ('title', 'time_create')


class PriceAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create')
    # list_filter = ('',)
    search_fields = ('title', 'time_create')


class CastAdmin(admin.ModelAdmin):
    list_display = ('title_banner', 'time_create')
    # list_filter = ('',)
    search_fields = ('title_banner', 'time_create')


class CastFotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create')
    # list_filter = ('',)
    search_fields = ('title', 'time_create')


class ElectroplatingAdmin(admin.ModelAdmin):
    list_display = ('title_banner', 'time_create')
    # list_filter = ('',)
    search_fields = ('title_banner', 'time_create')


class ElectroplatingFotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create')
    # list_filter = ('',)
    search_fields = ('title', 'time_create')


class SketchAdmin(admin.ModelAdmin):
    list_display = ('title_banner', 'time_create')
    # list_filter = ('',)
    search_fields = ('title_banner', 'time_create')



class SketchFotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create')
    # list_filter = ('',)
    search_fields = ('title', 'time_create')


class ModeledAdmin(admin.ModelAdmin):
    list_display = ('title_banner', 'time_create')
    # list_filter = ('',)
    search_fields = ('title_banner', 'time_create')


class ModeledFotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create')
    # list_filter = ('',)
    search_fields = ('title', 'time_create')

class ModeledVideoAdmin(admin.ModelAdmin):
    list_display = ('title_video', 'time_create')
    # list_filter = ('',)
    search_fields = ('title_video', 'time_create')


admin.site.register(BrieftDraft, BrieftDraftAdmin)
admin.site.register(Nature, NatureAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Diamond, DiamondAdmin)
admin.site.register(Clip, ClipdAdmin)
admin.site.register(Weddingrings, WeddingringsAdmin)
admin.site.register(Earring, EarringAdmin)
admin.site.register(Amulets, AmuletsAdmin)
admin.site.register(Ring, RingAdmin)
admin.site.register(CallbackRequest, CallbackRequestAdmin)
admin.site.register(Badge, BadgeAdmin)
admin.site.register(BadgeFoto, BadgeFotoAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Cast, CastAdmin)
admin.site.register(CastFoto, CastFotoAdmin)
admin.site.register(Electroplating, ElectroplatingAdmin)
admin.site.register(ElectroplatingFoto, ElectroplatingFotoAdmin)
admin.site.register(Sketch, SketchAdmin)
admin.site.register(SketchFoto, SketchFotoAdmin)
admin.site.register(Modeled, ModeledAdmin)
admin.site.register(ModeledFoto, ModeledFotoAdmin)
admin.site.register(ModeledVideo, ModeledVideoAdmin)