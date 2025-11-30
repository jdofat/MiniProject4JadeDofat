# django views:
# https://docs.djangoproject.com/en/5.2/topics/http/views/

# django render:
# https://docs.djangoproject.com/en/5.2/intro/tutorial03/#write-views-that-actually-do-something

# get_object_or_404 :
# https://docs.djangoproject.com/en/5.2/topics/http/shortcuts/#get-object-or-404

# get and post:
# https://docs.djangoproject.com/en/5.2/topics/forms/#the-view

# models/filtering:
# https://docs.djangoproject.com/en/5.2/topics/db/queries/#retrieving-specific-objects-with-filters

# field lookups:
# https://docs.djangoproject.com/en/5.2/ref/models/querysets/#icontains

#  context -- > templates:
# https://docs.djangoproject.com/en/5.2/intro/tutorial03/#passing-a-context

# pk lookup:
# https://docs.djangoproject.com/en/5.2/intro/tutorial03/#a-shortcut-get-object-or-404


# ----------------------------------------------------


from django.shortcuts import render, get_object_or_404
from .models import Internship

def home(request):
    return render(request, "internships/home.html")

def search(request):
    query = ""
    results = []

    if request.method == "POST":
        query = request.POST.get("q", "")
    elif request.method == "GET":
        query = request.GET.get("q", "")

    if query:
        results = Internship.objects.filter(title__icontains=query)

    return render(request, "internships/search.html", {
        "query": query,
        "results": results
    })

def detail(request, pk):
    internship = get_object_or_404(Internship, pk=pk)
    return render(request, "internships/detail.html", {"internship": internship})

def saved(request):
    return render(request, "internships/saved.html")
