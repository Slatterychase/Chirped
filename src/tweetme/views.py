from django.shortcuts import render

#Gets templater home.html
def home(request):
    return render(request, "home.html", {})