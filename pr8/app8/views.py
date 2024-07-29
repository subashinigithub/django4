from django.shortcuts import redirect, render
from django.http import HttpResponse
def new(r):
    return HttpResponse("Web-Development")
def page1(r):
    return render(r,"index.html",{'a':range(5)})
def page2(r):
    return render(r,"index1.html")

from .forms import *
def student_registration(request):
    

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the student form data
            student = form.save(commit=False)
            
            student.save()

            return redirect('home')  # Redirect to a success page
    else:
        form = StudentForm()
    
    return render(request, 'student/student_registration.html', {'form': form})



