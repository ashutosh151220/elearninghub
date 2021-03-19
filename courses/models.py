from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=150)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    description=models.CharField(max_length=500)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("published_at",)

    def __str__(self):
        return self.title

class Videos(models.Model):
    id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.URLField()


