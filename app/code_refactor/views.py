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
import os
import zipfile
import tempfile
import magic
import chardet

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers
from .utils import detect_language_from_filename
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


    """
    Handles the creation of code file instances.
    This includes processing uploaded ZIP files and extracting their contents.
    """
    def perform_create(self, serializer):
        project = serializer.save()

        if project.upload_type == 'zip' and project.uploaded_file:
            self.process_zip_file(project)


    """
    Processes a ZIP file uploaded as part of a project.
    This includes extracting the contents of the ZIP file and creating
    code file instances for each file within the ZIP.
    """
    def process_zip_file(self, project):
        zip_path = project.uploaded_file.path

        with tempfile.TemporaryDirectory() as tmpdirname:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(tmpdirname)

            for root, _, files in os.walk(tmpdirname):
                for file in files:
                    full_path = os.path.join(root, file)

                    # Skip binaries (e.g., images, compiled files)
                    mime_type = magic.from_file(full_path, mime=True)
                    if not mime_type.startswith('text'):
                        continue

                    try:
                        with open(full_path, 'rb') as f:
                            raw_bytes = f.read()
                            encoding = chardet.detect(raw_bytes)['encoding']
                            content = raw_bytes.decode(encoding or 'utf-8', errors='ignore')
                    except Exception as e:
                        print(f"Failed to read {full_path}: {e}")
                        continue

                    rel_path = os.path.relpath(full_path, tmpdirname)
                    language = detect_language_from_filename(file)

                    models.CodeFile.objects.create(
                        project=project,
                        path=rel_path,
                        language=language,
                        content=content
                    )


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


class MyUploadViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing MyUpload instances.
    """
    queryset = models.MyUpload.objects.all()
    serializer_class = serializers.MyUploadSerializer

    def create(self, request, *args, **kwargs):
        """
        Handles the creation of MyUpload instances.
        This includes processing uploaded files and creating code file instances.
        """
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        my_upload = serializer.save()
        print('path:', my_upload.file.path)
        return Response(serializer.data, status=status.HTTP_201_CREATED)