from django.shortcuts import render, redirect, get_object_or_404
from home.models import Task
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Home view with task creation form
@login_required
def home(request):
    context = {"success": False, "name": "Hafsa"}
    if request.method == "POST":
        # Handle the form submission to create a new task
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        if title and desc:
            # Assign the task to the current user
            ins = Task(title=title, desc=desc, user=request.user)
            ins.save()
            context = {"success": True}

    return render(request, 'index.html', context)

# View for listing all tasks for the logged-in user
@login_required
def tasks(request):
    allTasks = Task.objects.filter(user=request.user)  # Only get tasks for the current user
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)

# View for creating a new task
@login_required
def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        if title and desc:
            # Create task and assign to the logged-in user
            Task.objects.create(title=title, desc=desc, user=request.user)
        return redirect('tasks')
    return render(request, 'create_task.html')  # Template for creating a task

# View for editing a task
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Ensure task belongs to the user
    if request.method == "POST":
        task.title = request.POST.get('title', task.title)
        task.desc = request.POST.get('desc', task.desc)
        task.save()
        return redirect('tasks')
    context = {'task': task}
    return render(request, 'edit_task.html', context)  # Template for editing a task

# View for deleting a task
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Ensure task belongs to the user
    if request.method == "POST":
        task.delete()
        return redirect('tasks')
    context = {'task': task}
    return render(request, 'delete_task.html', context)  # Confirmation template for deletion

# View for toggling task status (completed/incomplete)
@login_required
def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Ensure task belongs to the user
    task.completed = not task.completed  # Toggle 'completed' status
    task.save()
    return redirect('tasks')
