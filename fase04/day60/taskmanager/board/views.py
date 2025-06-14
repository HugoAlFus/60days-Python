from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404


from .forms import TaskForm
from .models import Task

STATUSES = ['Por hacer', 'En progreso', 'Hecho']


@login_required
def board_view(request):
    tasks = Task.objects.all()
    return render(request, 'board/board.html', {
        'tasks': tasks,
        'statuses': STATUSES
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            error = "Usuario o contraseña incorrectos"
            return render(request, 'board/login.html', {'error': error})
    return render(request, 'board/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'board/register.html', {'form': form})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'board/task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # No guardes aún en BD
            task.user = request.user        # Asigna el usuario actual
            task.save()                     # Ahora sí guarda en la BD
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'board/task_form.html', {'form': form})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'board/task_form.html', {'form': form})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    # Si quieres, muestra una confirmación antes de borrar:
    return render(request, 'board/task_confirm_delete.html', {'task': task})


def logout_view(request):
    logout(request)
    return redirect('login')
