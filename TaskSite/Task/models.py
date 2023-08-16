from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify



class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="task_author")
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name="task_receiver")
    date = models.DateField(default=datetime.now)
    deadline = models.DateField()
    status = models.ForeignKey("Status",on_delete=models.CASCADE,default=0)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    def __str__(self):
        return self.name
    def generate_slug(self,name):
        base_slug = slugify(name)
        num = 1
        while Task.objects.filter(slug=base_slug).exists():
            base_slug = str(base_slug)+ '-' + str(num)
            num+=1
        return base_slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug(self.name)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('TaskView',kwargs={"task_slug":self.slug})
class Status(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,db_index=True,unique=True)
    def __str__(self):
        return self.name
class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="message_sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name="message_receiver")
    task = models.ForeignKey("Task",on_delete=models.CASCADE)
    status = models.ForeignKey("Status",on_delete=models.CASCADE)
    def __str__(self):
        return self.send.username + "to" + self.receive.username