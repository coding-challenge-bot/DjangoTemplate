from django.shortcuts import render

# del
def home(request):
    message = "Hello from Django!"
    return render(request, 'password_generator.html', {'message': message})
