from django.contrib import admin

# Register your models here.
from notes_app_exam.core.models import Profile, Note


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass