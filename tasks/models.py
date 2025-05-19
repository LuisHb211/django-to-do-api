from django.db import models


class TaskStatus(models.Model):
	name = models.CharField(max_length=65)
 
	def __str__(self):
		return self.name

class Task(models.Model):
	title = models.CharField(max_length=65, verbose_name=('Title'))
	description = models.CharField(max_length=165)
	created_at = models.DateTimeField(auto_now_add=True)
	finish_at = models.DateField()
	status = models.ForeignKey(
		TaskStatus, on_delete=models.SET_NULL, null=True, blank=True, default=None
	)
 
	def __str__(self):
		return self.title
	