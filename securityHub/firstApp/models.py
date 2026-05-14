from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Communities"
        verbose_name = "Community"

    def __str__(self):
        return self.name
    


class ResidentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    phone_number = models.CharField(max_length=15)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    




class SecurityOfficer(models.Model):
    name = models.CharField(max_length=100)
    badge_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    



class SecurityReport(models.Model):
    REPORT_TYPES = [
        ('Theft', 'Theft'),
        ('Fire', 'Fire'),
        ('Suspicious Activity', 'Suspicious Activity'),
    ]

    resident = models.ForeignKey(
        ResidentProfile,
        on_delete=models.CASCADE
    )

    officers = models.ManyToManyField(SecurityOfficer) 

    title = models.CharField(max_length=200)
    description = models.TextField()
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        