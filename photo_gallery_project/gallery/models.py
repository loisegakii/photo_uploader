from django.db import models
from django.contrib.auth.models import User

# This model represents a photo uploaded by a user
class Photo(models.Model):
    # Title of the photo, limited to 100 characters
    title = models.CharField(max_length=100)
    
    # The actual image file uploaded by the user.
    # Files will be saved in the 'photos/' directory inside MEDIA_ROOT
    image = models.ImageField(upload_to='photos/')
    
    # Optional text description of the photo
    description = models.TextField(blank=True)
    
    # Timestamp of when the photo was uploaded (automatically set)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    # Link to the user who uploaded the photo.
    # If the user is deleted, their photos will also be deleted
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    # When the model is displayed as a string (e.g., in admin), show the title
    def __str__(self):
        return self.title
