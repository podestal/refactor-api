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

from django.db import models


'''
Represents a project being analyzed or refactored.
Includes fields for the project name, description, upload type (ZIP or GitHub),
and the uploaded file or repository URL.
'''
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    upload_type = models.CharField(max_length=10, choices=[('zip', 'ZIP'), ('git', 'GitHub')])
    uploaded_file = models.FileField(upload_to='uploads/', null=True, blank=True)
    repo_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    analyzed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

''' 
Represents a file within a project, including its content and metadata.
Includes fields for the file path, programming language, content, AI-generated summary,
and complexity score.
'''
class CodeFile(models.Model):
    project = models.ForeignKey(Project, related_name='files', on_delete=models.CASCADE)
    path = models.CharField(max_length=500)  # Relative path inside the project
    language = models.CharField(max_length=50)
    content = models.TextField()
    ai_summary = models.TextField(blank=True)
    complexity_score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.project.name} - {self.path}"

'''
Represents a dependency relationship between two code files.
Includes fields for the source file, target file, and the type of dependency
(e.g., import, function call).
'''
class Dependency(models.Model):
    source_file = models.ForeignKey(CodeFile, related_name='outgoing_dependencies', on_delete=models.CASCADE)
    target_file = models.ForeignKey(CodeFile, related_name='incoming_dependencies', on_delete=models.CASCADE)
    dependency_type = models.CharField(max_length=50)  # import, function_call, etc.

    def __str__(self):
        return f"{self.source_file.path} -> {self.target_file.path}"

'''
Represents an external service (e.g., API, database) used by a project or file.
Includes fields for the project, file, service type, protocol, endpoint,
and method (e.g., GET, POST).
'''
class ExternalService(models.Model):
    project = models.ForeignKey(Project, related_name='services', on_delete=models.CASCADE)
    file = models.ForeignKey(CodeFile, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50)  # API, DB, Queue, etc.
    protocol = models.CharField(max_length=20, blank=True)  # HTTP, SQL, etc.
    endpoint = models.CharField(max_length=255)  # e.g., URL or DB table
    method = models.CharField(max_length=10, blank=True)  # GET, POST, SELECT, etc.

    def __str__(self):
        return f"{self.service_type} in {self.file.path}"