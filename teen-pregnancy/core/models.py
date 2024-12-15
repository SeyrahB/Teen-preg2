from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Resource Model
class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(max_length=200, default='http://example.com')  # Set a default value here.
    category = models.CharField(max_length=100, choices=[('Health', 'Health'), ('Support', 'Support'), ('Education', 'Education')])

    def __str__(self):
        return self.title
# Forum Post Model
class ForumPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(ForumPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.post.title}"   

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]