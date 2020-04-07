# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (
   SFTPUser,
   SFTPUserKey,
   FileHistory,
   FileValidator,
)


@admin.register(SFTPUser)
class SFTPUserAdmin(admin.ModelAdmin):
    pass


@admin.register(SFTPUserKey)
class SFTPUserKeyAdmin(admin.ModelAdmin):
    pass


@admin.register(FileHistory)
class FileHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(FileValidator)
class FileValidatorAdmin(admin.ModelAdmin):
    pass



