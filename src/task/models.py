from django.db import models
from django.utils.text import slugify
import random
from django.db import IntegrityError
from django.core.urlresolvers import reverse
# Create your models here.
class Tag(models.Model):
    slug = models.SlugField()

    def __unicode__(self):
        return self.slug

class Task(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(editable=False,auto_now_add=True)
    updated = models.DateTimeField(editable=False, auto_now=True )
    deadline = models.DateTimeField(editable=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created', 'title']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        try:
            obj = Task.objects.filter(slug__contains=self.slug)
            if obj:
                new = obj[0].slug.split('-')[-1]
                new = int(new)+1
                self.slug = self.slug+'-'+str(new)
            super(Task, self).save(*args, **kwargs)
        except IntegrityError:
            raise IntegrityError

    def get_absolute_url(self):
        return reverse('task:detail', kwargs={'slug':self.slug})


