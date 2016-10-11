from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    paragraphs = Paragraphs.objects.first()
    work_categories = WorkCategory.objects

    context = {
        'paragraphs': paragraphs,
        'work_categories': work_categories,
    }

    return render(request, 'website/index.html', context)


def tornitura(request):
    paragraphs = Paragraphs.objects.first()
    work_machines = Machine.objects.filter(work_category__name="Tornitura")

    context = {
        'paragraphs': paragraphs,
        'work_machines': work_machines,
    }

    return render(request, 'website/tornitura.html', context)


def fresatura(request):
    paragraphs = Paragraphs.objects.first()
    work_machines = Machine.objects.filter(work_category__name="Fresatura")

    context = {
        'paragraphs': paragraphs,
        'work_machines': work_machines,
    }

    return render(request, 'website/fresatura.html', context)


def tmachine(request, machine_id):
    machine = Machine.objects.get(id=machine_id)
    images = MachineImage.objects.filter(machine__id=machine_id)
    paragraphs = Paragraphs.objects.first()

    context = {
        'machine': machine,
        'images': images,
        'paragraphs': paragraphs,
    }

    return render(request, 'website/machine.html', context)


def fmachine(request, machine_id):
    machine = Machine.objects.get(id=machine_id)
    images = MachineImage.objects.filter(machine__id=machine_id)
    paragraphs = Paragraphs.objects.first()

    context = {
        'machine': machine,
        'images': images,
        'paragraphs': paragraphs,
    }

    return render(request, 'website/machine.html', context)


def gallery(request):
    albums = Album.objects.all()
    paragraphs = Paragraphs.objects.first()

    context = {
        'albums': albums,
        'paragraphs': paragraphs,
    }

    return render(request, 'website/gallery.html', context)


def album(request, album_id):
    gallery_album = Album.objects.filter(id=album_id).first()
    album_images = Image.objects.filter(album__id=album_id)
    paragraphs = Paragraphs.objects.first()

    context = {
        'gallery_album': gallery_album,
        'album_images': album_images,
        'paragraphs': paragraphs,
    }

    return render(request, 'website/album.html', context)


def image(request, album_id, image_id):
    gallery_album = Album.objects.filter(id=album_id).first()
    gallery_image = Image.objects.filter(id=image_id).first()
    paragraphs = Paragraphs.objects.first()

    context = {
        'gallery_album': gallery_album,
        'gallery_image': gallery_image,
        'paragraphs': paragraphs,
    }

    return render(request, 'website/image.html', context)
