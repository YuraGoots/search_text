from django.db import models



# Create your models here.
class Search(models.Model):
    searching_text = models.CharField('Search text', max_length=150, default='put search text here')
    email = models.EmailField('E-mail to send response', default='put your email here')
    t_limit = models.PositiveSmallIntegerField('Time limit, sec', default=60)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.email


class TextSegment(models.Model):
    text = models.TextField()
    book = models.CharField(max_length=300)
    chapter = models.CharField(max_length=300)
    page = models.IntegerField()

    def __unicode__(self):
        return self.book
