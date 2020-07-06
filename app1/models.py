from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class add(models.Model):
	user = models.ForeignKey(get_user_model(),
        null=True,on_delete=models.CASCADE)
	task = models.CharField(max_length=30)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.task,self.user
