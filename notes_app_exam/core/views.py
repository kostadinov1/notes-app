from django.shortcuts import render, redirect

# Create your views here.
from notes_app_exam.core.forms import NoteCreateForm, NoteEditForm, NoteDeleteForm, ProfileCreateForm, ProfileDeleteForm
from notes_app_exam.core.models import Profile, Note


def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile
    else:
        return False

def home_page(request):
    profile = get_profile()
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    if not profile:
        return redirect('login')

    return render(request, 'home-with-profile.html', context)


def login_page(request):
    return render(request, 'home-no-profile.html')


def add_note(request):
    if request.method == 'POST':
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = NoteCreateForm()
    context = {
        'form': form
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteEditForm(instance=note)
    context = {
        'form': form,
        'note': note
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = NoteDeleteForm(request.POST, instance=note)
        context = {
            'form': form,
            'note': note
        }
        return render(request, 'note-delete.html', context)
    else:
        note.delete()
        return redirect('home')


def details_note(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)


def profile_page(request):
    profile = get_profile()
    notes_count = len(Note.objects.all())
    context = {
        'profile': profile,
        'notes_count': notes_count
    }

    return render(request, 'profile.html', context)

# NO TEMPLATE MADE FOR THIS VIEW

# def delete_profile_page(request):
#     profile = get_profile()
#     if request.method == 'GET':
#         form = ProfileDeleteForm(request.POST, instance=profile)
#         context = {
#             'form': form,
#             'profile': profile
#         }
#         return render(request, 'profile-delete.html')
#
#     else:
#         profile.delete()
#         return redirect('home')
