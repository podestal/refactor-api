# # This file is part of the Code Refactor project.
# # The project is licensed under the MIT License.
# # For more details, see the LICENSE file in the root directory of this project.

# from django.db import models

# class Project(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     upload_type = models.CharField(max_length=10, choices=[('zip', 'ZIP'), ('git', 'GitHub')])
#     uploaded_file = models.FileField(upload_to='uploads/', null=True, blank=True)
#     repo_url = models.URLField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     analyzed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name

# class CodeFile(models.Model):
#     project = models.ForeignKey(Project, related_name='files', on_delete=models.CASCADE)
#     path = models.CharField(max_length=500)  # Relative path inside the project
#     language = models.CharField(max_length=50)
#     content = models.TextField()
#     ai_summary = models.TextField(blank=True)
#     complexity_score = models.FloatField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.project.name} - {self.path}"

# class Dependency(models.Model):
#     source_file = models.ForeignKey(CodeFile, related_name='outgoing_dependencies', on_delete=models.CASCADE)
#     target_file = models.ForeignKey(CodeFile, related_name='incoming_dependencies', on_delete=models.CASCADE)
#     dependency_type = models.CharField(max_length=50)  # import, function_call, etc.

#     def __str__(self):
#         return f"{self.source_file.path} -> {self.target_file.path}"

# class ExternalService(models.Model):
#     project = models.ForeignKey(Project, related_name='services', on_delete=models.CASCADE)
#     file = models.ForeignKey(CodeFile, on_delete=models.CASCADE)
#     service_type = models.CharField(max_length=50)  # API, DB, Queue, etc.
#     protocol = models.CharField(max_length=20, blank=True)  # HTTP, SQL, etc.
#     endpoint = models.CharField(max_length=255)  # e.g., URL or DB table
#     method = models.CharField(max_length=10, blank=True)  # GET, POST, SELECT, etc.

#     def __str__(self):
#         return f"{self.service_type} in {self.file.path}"

