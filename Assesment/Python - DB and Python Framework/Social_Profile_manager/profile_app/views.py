from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserProfileForm
from .models import UserProfile
from django.http import HttpResponse
import csv

# Create your views here.

def create_profile(request):

    if request.method == "POST":

        form = UserProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('profile_list')

    else:
        form = UserProfileForm()

    return render(request, 'create_profile.html', {'form': form})

def profile_list(request):
    profiles = UserProfile.objects.all()

    return render(
        request,
        'profile_list.html',
        {'profiles': profiles}
    )

def update_profile(request, profile_id):
    profile = get_object_or_404(UserProfile, id=profile_id)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile_list')

    else:
        form = UserProfileForm(instance=profile)

    return render(
        request,
        'update_profile.html',
        {
            'form': form,
            'profile': profile
        }
    )

def delete_profile(request, profile_id):
    profile = get_object_or_404(UserProfile, id=profile_id)

    if request.method == "POST":
        profile.delete()
        return redirect('profile_list')

    return render(
        request,
        'delete_profile.html',
        {'profile': profile}
    )

def export_profiles(request):

    response = HttpResponse(content_type='text/csv')

    response['Content-Disposition'] = 'attachment; filename="profiles.csv"'

    writer = csv.writer(response)

    writer.writerow([
        'Username',
        'Age',
        'Public Status'
    ])

    profiles = UserProfile.objects.all()

    for profile in profiles:
        writer.writerow([
            profile.username,
            profile.age,
            profile.is_public
        ])

    return response
