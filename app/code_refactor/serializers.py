'''
This module defines the database models for the code refactoring application.
These models represent the core entities involved in the analysis and refactoring
process, including projects, code files, dependencies, and external services.
Each model is defined as a class that inherits from `django.db.models.Model`.
The models include:
- `Project`: Represents a project being analyzed or refactored.
- `CodeFile`: Represents a file within a project, including its content and metadata.
- `Dependency`: Represents a dependency relationship between two code files.
- `ExternalService`: Represents an external service (e.g., API, database) used by a project or file.
'''

from . import models
from rest_framework import serializers

'''
Represents a project being analyzed or refactored.
Includes fields for the project name, description, upload type (ZIP or GitHub),
and the uploaded file or repository URL.
'''

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'


'''
Represents a file within a project, including its content and metadata.
Includes fields for the file path, programming language, content, AI-generated summary,
and complexity score.
'''
class CodeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CodeFile
        fields = '__all__'


'''
Represents a dependency relationship between two code files.
Includes fields for the source file, target file, and the type of dependency
(e.g., import, function call).
'''
class DependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dependency
        fields = '__all__'

        
'''
Represents an external service (e.g., API, database) used by a project or file.
Includes fields for the service name, type, and any relevant configuration details.
'''
class ExternalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExternalService
        fields = '__all__'
