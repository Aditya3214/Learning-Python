from django.shortcuts import render,redirect
from .models import Student

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        grade = request.POST.get('grade')

        if name and grade:
            Student.objects.create(name=name,grade=grade)
            return redirect('/')

    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

