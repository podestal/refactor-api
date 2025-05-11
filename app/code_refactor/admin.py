from django.contrib import admin
from . import models

admin.site.register(models.Project)
admin.site.register(models.CodeFile)
admin.site.register(models.Dependency)
admin.site.register(models.ExternalService)
admin.site.register(models.MyUpload)
