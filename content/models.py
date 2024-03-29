from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Select, FileInput
from django.urls import reverse

from django.utils.safestring import mark_safe
# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from product.models import Product


class Menu(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children',on_delete=models.CASCADE)

    title = models.CharField(max_length=100,unique=True)
    link = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, choices= STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::1])


class Content(models.Model):
    TYPE = (
        ('menu', 'menu'),
        ('haber', 'haber'),
        ('duyuru', 'duyuru'),
        ('etkinlik', 'etkinlik'),

    )
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),

    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.OneToOneField(Menu,null=True,blank=True,on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=TYPE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')
    detail = RichTextUploadingField()
    slug = models.SlugField(null=False,unique=True)
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.title

    def image_tag(self):
        return mark_safe(' <img src = "{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('content_detail',kwargs={'slug':self.slug})

class ContentForm(ModelForm):
    class Meta:
        TYPE = (
            ('menu', 'menu'),
            ('haber', 'haber'),
            ('duyuru', 'duyuru'),
            ('etkinlik', 'etkinlik'),

        )
        model = Content
        fields = ['type','title','slug','keywords','description','image','detail']
        widgets = {
            'title' : TextInput(attrs={'class':'input','placeholder':'title'}),
            'slug' : TextInput(attrs={'class':'input','placeholder':'slug'}),
            'keywords' : TextInput(attrs={'class':'input','placeholder':'keywords'}),
            'description' : TextInput(attrs={'class':'input','placeholder':'description'}),
            'type' : Select(attrs={'class':'input','placeholder':'city'},choices = TYPE ),
            'image' : FileInput(attrs={'class':'input','placeholder':'image'}),
            'detail' : CKEditorWidget(),
        }



class CImages(models.Model):
    content = models.ForeignKey(Content,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True,upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe(' <img src = "{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class ContentImageForm(ModelForm):
    class Meta:
        model = CImages
        fields = ['title','image']



















