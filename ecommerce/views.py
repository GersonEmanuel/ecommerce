from django.shortcuts import render

# Create your views here.
def home_page(request):
    context={'title': 'pricipal page', 'content':'principal'}
    return render(request, 'index.html', context)

def about_page(request):
    context = {'title':'about page', 'content':
               'welcome to about page'}
    return render(request, 'about_page.html', context)

def contact_page(request):
    context = {'title': 'contact page', 'content':'Welcome contact page'}
    return render(request, 'contact_page.html', context)
