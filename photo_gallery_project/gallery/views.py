from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from .models import Photo


# -----------------------------
# User Registration View
# -----------------------------
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        # Password match validation
        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Check for duplicate username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        # Create user account
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully. You can now log in.")
        return redirect('login')

    return render(request, 'gallery/register.html')


# -----------------------------
# User Login View
# -----------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('photo_list')  # Redirect to /photos/ after login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'gallery/login.html')


# -----------------------------
# Logout View
# -----------------------------
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


# -----------------------------
# Homepage View (Public)
# -----------------------------
def home_view(request):
    return render(request, 'gallery/home.html')


# -----------------------------
#  Profile View (Authenticated Only)
# -----------------------------
@login_required
def profile_view(request):
    return render(request, 'gallery/profile.html')


# -----------------------------
# Upload Photo View (Authenticated Only)
# -----------------------------
@login_required
def upload_photo_view(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploaded_by = request.user
            photo.save()
            messages.success(request, "Photo uploaded successfully!")
            return redirect('photo_list')
    else:
        form = PhotoForm()

    return render(request, 'gallery/upload.html', {'form': form})


# -----------------------------
# View All Uploaded Photos
# -----------------------------
@login_required
def photo_list_view(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    welcome_message = f"Welcome, {request.user.username}!"
    return render(request, 'gallery/photos.html', {'photos': photos, 'welcome_message': welcome_message
    })

