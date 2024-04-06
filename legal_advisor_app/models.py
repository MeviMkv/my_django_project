# In legal_advisor_app/models.py

from django.db import models
from django.contrib.auth.models import User

class LegalDocument(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class DocumentTemplate(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Client(models.Model): 
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Case(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()

    def __str__(self):
        return self.title

class LegalResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    document = models.FileField(upload_to='legal_resources/')

    def __str__(self):
        return self.title
