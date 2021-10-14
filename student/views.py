from django.shortcuts import redirect, render
from student.forms import StudentForm
from django.contrib import messages

def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successful")
            return redirect('index')  #post(submit) sonrası yönlendirilecek page'i yazıyoruz.
            
    form = StudentForm()
    context = {
        'form' : form
    }
    
    return render(request,'student/student.html', context)
