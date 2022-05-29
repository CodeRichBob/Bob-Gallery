from django.shortcuts import render

# Create your views here.

def gallery(request):
    location = request.GET.get('location')

    if location ==  None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(location__name = location)



    categories = Category.objects.all()
    locations = Location.objects.all()

    return render(request,'photos/gallery.html', {"categories" : categories,"photos" : photos,"locations" : locations})
