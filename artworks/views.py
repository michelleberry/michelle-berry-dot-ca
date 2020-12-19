from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import collection, artPiece

# Create your views here.
def start(request):
    return render(request, 'artworks/start.html', {})

def choose_gallery(request):
    collection_list = collection.objects.all()
    template = loader.get_template('artworks/choose_gallery.html')
    context = {
        'collection_list': collection_list,
    }
    return HttpResponse(template.render(context, request))

def collection_index(request, pk):
    thisCollection = collection.objects.get(pk=pk)
    artPieces = thisCollection.artpiece_set.all()
    template = loader.get_template('artworks/collection_index.html')
    context = {
        'artPieces': artPieces,
        'thisCollection': thisCollection
    }
    return HttpResponse(template.render(context,request))

def art_details(request, collection_id, art_id):
    thisCollection = collection.objects.get(pk=collection_id)
    artPiece = thisCollection.artpiece_set.get(pk=art_id)
    template = loader.get_template('artworks/art_details.html')
    context = {
        'artPiece': artPiece,
        'thisCollection': thisCollection
    }
    return HttpResponse(template.render(context,request))
