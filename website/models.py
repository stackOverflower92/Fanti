from __future__ import unicode_literals

from django.db import models

'''
_________________________________________________________________________________

MODELS USED FOR IMAGES
_________________________________________________________________________________

'''


class Gallery(models.Model):
    class Meta:
        verbose_name = "Galleria"
        verbose_name_plural = "Gallerie"

    title = models.CharField(max_length=200)
    caption = models.TextField()

    def __str__(self):
        return self.title.encode('utf8')


class Album(models.Model):
    class Meta:
        verbose_name = "Album di Immagini"
        verbose_name_plural = "Album di Immagini"

    title = models.CharField(max_length=200)
    caption = models.TextField()
    gallery = models.ForeignKey(Gallery, models.CASCADE)

    def __str__(self):
        return self.title.encode('utf8')


class Image(models.Model):
    class Meta:
        verbose_name = "Immagine"
        verbose_name_plural = "Immagini"

    file = models.ImageField(upload_to="uploads/images/gallery")
    title = models.CharField(max_length=200)
    caption = models.TextField()
    album = models.ForeignKey(Album, models.CASCADE)

    def __str__(self):
        return self.title.encode('utf8')


'''
_________________________________________________________________________________

MODELS USED FOR MACHINES

WorkCategory = Tornitura/Fresatura/...
Machine = Actual machine
MachineImage = Image for machine
_________________________________________________________________________________

'''


class WorkCategory(models.Model):
    class Meta:
        verbose_name = "Tipo di Lavorazione"
        verbose_name_plural = "Tipi di Lavorazione"

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.encode('utf8')


class Machine(models.Model):
    class Meta:
        verbose_name = "Macchina"
        verbose_name_plural = "Macchine"

    name = models.CharField(max_length=200)
    details = models.TextField(max_length=200)
    work_category = models.ForeignKey(WorkCategory, models.CASCADE)

    def __str__(self):
        return self.name.encode('utf8')


class MachineImage(models.Model):
    class Meta:
        verbose_name = "Immagine per Macchina"
        verbose_name_plural = "Immagini per Macchina"

    file = models.ImageField(upload_to="uploads/machine_images")
    name = models.CharField(max_length=200)
    machine = models.ForeignKey(Machine, models.CASCADE)

    def __str__(self):
        return self.name.encode('utf8')


'''
_________________________________________________________________________________

MODELS USED FOR TEXTS AND DESCRIPTIONS

It is a singleton
_________________________________________________________________________________

'''


class Paragraphs(models.Model):
    class Meta:
        verbose_name = "Gruppo di Descrizioni e Paragrafi del Sito"
        verbose_name_plural = "Gruppi di Descrizioni e Paragrafi del Sito"

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(Paragraphs, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()

    site_name = models.CharField(max_length=200)
    site_description = models.TextField()
    site_bio = models.TextField()
    header_image = models.ImageField(upload_to="uploads/images/paragraphs")
    gallery_image = models.ImageField(upload_to="uploads/images/paragraphs")
    tornitura_image = models.ImageField(upload_to="uploads/images/paragraphs")
    fresatura_image = models.ImageField(upload_to="uploads/images/paragraphs")
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    piva = models.CharField(max_length=100)
    tornitura_description = models.TextField()
    fresatura_description = models.TextField()

    def __str__(self):
        return "Descrizioni e Paragrafi"