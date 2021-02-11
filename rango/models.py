from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User

#created the two initial data models for the Rango application
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    # replaces whitespace with hyphens using slugify function
    slug = models.SlugField(unique=True)

    #override the save method, this new function will call slugify function and update new slug field with it
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    #typo within admin interface can be fixed using code below.On the page, it was Categorys instead of Categories
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    #CASCADE instructs Django to delete the pages associated with the category when the category is deleted
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    #Django will display the string representation of the object, derived from __str__(). adding __str()__ will make debugging easy too
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    #links UserProfile to a user model instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional attributes we wanna include
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username