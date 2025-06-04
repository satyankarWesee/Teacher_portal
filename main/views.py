from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student
from .forms import StudentForm

def login_view(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            if not username or not password:
                messages.error(request, "Username and password are required.")
                return render(request, 'main/login.html')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid credentials")
        except Exception as e:
            messages.error(request, "An unexpected error occurred. Please try again.")
    return render(request, 'main/login.html')

@login_required
def dashboard(request):
    try:
        students = Student.objects.all()
        form = StudentForm()
    except Exception as e:
        messages.error(request, "Failed to load student data. Please try again later.")
        students = []
        form = StudentForm()
    
    return render(request, 'main/dashboard.html', {'students': students, 'form': form})

@login_required
def logout_view(request):
    try:
        logout(request)
        messages.success(request, "You have been logged out successfully.")
    except Exception as e:
        messages.error(request, "An error occurred during logout. Please try again.")
    return redirect('login')

@login_required
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        subject = request.POST.get('subject').strip()
        marks = request.POST.get('marks')

        try:
            marks = int(marks)
            if marks < 0:
                messages.error(request, "Marks cannot be negative.")
                return redirect('dashboard')
        except ValueError:
            messages.error(request, "Marks must be a number.")
            return redirect('dashboard')


        marks = int(marks)

        try:
            # Try to find existing student
            student = Student.objects.get(name=name, subject=subject)
            student.marks += marks
            student.save()
            messages.success(request, f"Updated marks for {name} in {subject}.")
        except Student.DoesNotExist:
            # Create new student if not found
            Student.objects.create(name=name, subject=subject, marks=marks)
            messages.success(request, f"Added new student {name} for {subject}.")
        
        return redirect('dashboard')



@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        name = request.POST.get('name').strip()
        subject = request.POST.get('subject').strip()
        marks = request.POST.get('marks')

        try:
            marks = int(marks)
            if marks < 0:
                messages.error(request, "Marks cannot be negative.")
                return redirect('dashboard')
        except ValueError:
            messages.error(request, "Marks must be a number.")
            return redirect('dashboard')

        if Student.objects.filter(name=name, subject=subject).exclude(id=student.id).exists():
            messages.error(request, f"A student with the name '{name}' and subject '{subject}' already exists.")
            return redirect('dashboard')

        student.name = name
        student.subject = subject
        student.marks = marks
        student.save()
        messages.success(request, f"{name}'s record updated successfully.")
        
    return redirect('dashboard')


@login_required
def delete_student(request, id):
    try:
        student = get_object_or_404(Student, id=id)
        student.delete()
        messages.success(request, "Student deleted successfully.")
    except Exception as e:
        messages.error(request, "Failed to delete student. Please try again.")
    return redirect('dashboard')
