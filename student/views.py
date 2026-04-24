from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from .forms import StudentForm
from django.db.models import Q

def home(request):
    return render(request, 'student/landing.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'student/signup.html', {
        'form': form,
        'hide_login_button': True,  
    })

class CustomLoginView(LoginView):
    template_name = 'student/login.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Successfully logged in!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_login_button'] = True 
        return context

@login_required
def dashboard(request):
    query = request.GET.get('q', '').strip()
    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) | Q(usn__icontains=query)
        )
    else:
        students = Student.objects.all()
    
    context = {
        'students': students,
        'hide_dashboard_nav': True
    }

    return render(request, 'student/dashboard.html', context)

@login_required
def create_student(request, id=None):
    student = get_object_or_404(Student, id=id) if id else None
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            if student:  
                messages.success(request, f'Student record for {form.instance.name} updated successfully!')
            else: 
                messages.success(request, f'New student record for {form.instance.name} created successfully!')
            return redirect('dashboard')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/student_form.html', {'form': form})

@login_required
def view_student(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student/view_student.html', {'student': student})

@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student record deleted successfully!')
        return redirect('dashboard')
    return render(request, 'student/confirm_delete.html', {'student': student})