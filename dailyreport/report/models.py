from django.db import models
from datetime import date,datetime
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Work(models.Model):
    content=models.TextField(blank=False)
    date=models.DateField(default=datetime.now, blank=False)
    create_at=models.DateTimeField(default=datetime.now, blank=True)
    update_at=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self): 
        return self.content

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    
    def __str__(self):
        # return f'{self.user.username} Profile'
        return self.user.username


    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :
            output_size = (300 , 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        # img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300 :
        #     output_size = (300 , 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)
