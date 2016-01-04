from __future__ import unicode_literals

from django.db import models

class HomePage(models.Model):
    header = models.CharField(max_length=1000)
    content_title = models.CharField(max_length=200)
    content = models.TextField()
    resume = models.FileField(default=None, blank=True)

    def __str__(self):
    	return "Homepage"

class HomePageImage(models.Model):
    homepage = models.ForeignKey(HomePage, related_name='images')
    title = models.CharField(max_length=200)
    image = models.ImageField('Image')
    
    def imageLink(self):
        if self.Image:
            return '<a href="' + str(self.Image.url) + '">' + 'NameOfFileGoesHere' + '</a>'
        else:
            return '<a href="''"></a>'

    imageLink.allow_tags = True
    imageLink.short_description = "Image Link"

    def image_tag(self):
        return u'<img src="%s" width="300px" height="auto" />' % str(self.image.url)
        #return u'Yo! I hacked you!'

    image_tag.allow_tags = True
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title
