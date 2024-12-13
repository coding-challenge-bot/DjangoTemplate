from django.shortcuts import render


# del
def home(request):
    message = "Home page"
    return render(request, 'password_generator.html', {'message': message})
