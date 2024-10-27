from django.shortcuts import render

# Create your views here.
def cart_home(request):
    request.session['cart_id'] = 123
    request.session['user'] = request.user.username
    return render(request, 'home.html', {})
