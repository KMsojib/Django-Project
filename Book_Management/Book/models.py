from django.db import models

# Create your models here.
class BookStoreModel(models.Model):
    CATAGORY = (
        ('Historical fiction','Historical fiction'),
        ('Fantasy','Fantasy'),
        ('Romance','Romance'),
        ('Comics','Comics'),
        ('Short Story','Short Story'),
        ('Memoir','Memoir'),
        ('Magical Realism','Magical Realism'),
        ('Horror','Horror'),
        ('Mystery','Mystery'),
        ('Biography','Biography'),
        ('Dystopian','Dystopian'),
        ('CookBook','CookBook'),
        ('Paranormal Activity','Paranormal Activity'),
        ('History','History'),    
    )
    BookID = models.IntegerField(primary_key=True)
    Book_Name = models.CharField(max_length = 30)
    Catagory = models.CharField(max_length = 30, choices = CATAGORY)
    Author = models.CharField(max_length = 30)
    First_publication = models.DateTimeField(auto_now_add = True)
    Last_publication = models.DateTimeField()