from django.db import models
from django.contrib.auth.models import User

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    purpose_of_visit = models.TextField()
    visit_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class VisitRequest(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Waiting'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visit Request for {self.visitor.name} by {self.receiver.username}"
