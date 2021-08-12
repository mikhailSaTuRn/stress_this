from django.db import models

# Create your models here.
class Words(models.Model):
    word = models.CharField(max_length=100)
    stress_idx = models.IntegerField(default=0)
    stress_extra_idx = models.IntegerField(default=0)
    example = models.TextField(default="*калі будзе што, то дадам*")
    article = models.TextField(default="*калі будзе што, то дадам*")



