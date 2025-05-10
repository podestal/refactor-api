'''
This module defines the views for the code refactoring application.
These views use Django REST Framework's viewsets to create RESTful endpoints
for the various models in the application.
The views include:
- `ProjectViewSet`: Endpoint for managing projects.
- `CodeFileViewSet`: Endpoint for managing code files.
- `DependencyViewSet`: Endpoint for managing dependencies.
- `ExternalServiceViewSet`: Endpoint for managing external services.     
'''


from . import models
from . import serializers
from rest_framework import viewsets


'''
Represents a project being analyzed or refactored.
Includes fields for the project name, description, upload type (ZIP or GitHub),
and the uploaded file or repository URL.
'''
class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing project instances.
    """
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


'''
Represents a file within a project, including its content and metadata.
Includes fields for the file path, programming language, content, AI-generated summary,
and complexity score.
'''
class CodeFileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing code file instances.
    """
    queryset = models.CodeFile.objects.all()
    serializer_class = serializers.CodeFileSerializer


'''
Represents a dependency relationship between two code files.
Includes fields for the source file, target file, and the type of dependency
(e.g., import, function call).
'''
class DependencyViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dependency instances.
    """
    queryset = models.Dependency.objects.all()
    serializer_class = serializers.DependencySerializer


'''
Represents an external service (e.g., API, database) used by a project or file.
Includes fields for the service name, type, and any relevant configuration details.
'''
class ExternalServiceViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing external service instances.
    """
    queryset = models.ExternalService.objects.all()
    serializer_class = serializers.ExternalServiceSerializer
    