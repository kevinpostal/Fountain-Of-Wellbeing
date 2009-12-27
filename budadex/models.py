from django.db import models
import os
import settings

#import pdb; pdb.set_trace()
# Create your models here.

class Strain(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='strain_images/',blank=True,null=True)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    thumbnail = models.ImageField(upload_to='strain_images/thumbnails/',editable=False)
    active = models.BooleanField()
    
    def save(self):
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile

        #Makes sure theres even a photo to Convert
        if self.photo:
        
            #Save instance of Photo  
            super(Strain, self).save() 

            #Original Photo  
            imgFile = Image.open(self.photo.path)
        
            #convert to RGB
            if imgFile.mode not in ('L', 'RGB'):  
                imgFile = imgFile.convert('RGB')
       
            # Set our max thumbnail size in a tuple (max width, max height)   
            THUMBNAIL_SIZE = (200, 200)

       
            # We use our PIL Image object to create the thumbnail, which already
            # has a thumbnail() convenience method that contrains proportions.
            # Additionally, we use Image.ANTIALIAS to make the image look better.
            # Without antialiasing the image pattern artifacts may result.

            imgFile.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
        
            temp_handle = StringIO()
            imgFile.save(temp_handle, 'png')
            temp_handle.seek(0)
        
            # Save To the thumbnail field
            suf = SimpleUploadedFile(os.path.split(self.photo.name)[-1],
                    temp_handle.read(), content_type='image/png')
            self.thumbnail.save(suf.name+'.png', suf, save=False)

        #Save instance of Photo  
        super(Strain, self).save() 
        
    def thumb_photo(self):

        return '<img src = %s%s height="150" width="150"></img>' % (settings.MEDIA_URL,self.thumbnail)
    thumb_photo.allow_tags=True