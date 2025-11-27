from django.db import models
from django.contrib.auth.models import User   #User model import kiya

class Grievance(models.Model):
    
    # 1. --- Categories of Greivance ---
    CATEGORY_CHOICES = [
        ('ROAD', 'Road & Transport'),
        ('WATER', 'Water Supply'),
        ('ELECTRICITY', 'Electricity & Street Lights'),
        ('GARBAGE', 'Garbage & Cleaning'),
        ('OTHER', 'Other'),
    ]

    # 2. --- Status of Grievance ---
    STATUS_CHOICES = [
        ('PENDING', 'Pending Review'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('REJECTED', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Complaint Subject")
    description = models.TextField(verbose_name="Detailed Issue")

    # 3. New Field: Name of Location
    location = models.CharField(max_length=200, help_text="E.g., Sector 4, Main Market")

    # 4. Photo for Proof
    evidence_image = models.ImageField(upload_to='grievances/', blank=True, null=True)

    # 5. Category and Status
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.status}"
# Create your models here.
