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
