from rest_framework_nested import routers
from . import views

'''
This module defines the URL routing for the code refactoring application.
It uses Django REST Framework's router to create RESTful endpoints for the
various models in the application.
The URL patterns include:
- `/api/projects/`: Endpoint for managing projects.
- `/api/codefiles/`: Endpoint for managing code files.
- `/api/dependencies/`: Endpoint for managing dependencies.
- `/api/externalservices/`: Endpoint for managing external services.
'''

router = routers.DefaultRouter()
router.register('projects', views.ProjectViewSet, basename='projects')
router.register('codefiles', views.CodeFileViewSet, basename='codefiles')
router.register('dependencies', views.DependencyViewSet, basename='dependencies')
router.register('externalservices', views.ExternalServiceViewSet, basename='externalservices')
urlpatterns = router.urls
