from django.db import models

#created the two initial data models for the Rango application
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)


    #typo within admin interface can be fixed using code below.On the page, it was Categorys instead of Categories
    class Meta:
        verbose_name_plural = 'Categories'

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
