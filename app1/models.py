from django.db import models

class add(models.Model):
	task = models.CharField(max_length=30)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.task
