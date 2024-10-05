from django.shortcuts import render,redirect
from django.http import HttpResponse
from quota.models import Subject,Student,registerSubject
from django.contrib.auth.models import User
from users import views
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request,'index.html')

def subject_list(request):
    all_subject = Subject.objects.all()
    return render(request, 'subject_list.html', {
        "all_subject": all_subject,
    })

def my_quota(request):
    mySubject = registerSubject.objects.filter(username=request.user.username)
    return render(request, 'my_quota.html', {
        "mySubject": mySubject,
    })

from django.shortcuts import get_object_or_404

from django.db import transaction

@transaction.atomic
def add_subject(request, id):
    # Get the subject details from the Subject model
    subject = get_object_or_404(Subject, subjectCode=id)

    # Check if there are seats available
    if subject.seatAvailable <= 0:
        messages.error(request, "No seats available for this subject.")
        return redirect('my_quota')  

    # Check if the subject has already been added
    if registerSubject.objects.filter(username=request.user.username, subjectCode=id).exists():
        messages.error(request, "This subject has already been added to your quota.")
        return redirect('my_quota')  

    # Create a new registerSubject entry with all necessary details
    addSubject = registerSubject.objects.create(
        username=request.user.username,
        subjectCode=subject.subjectCode,
        subjectName=subject.subjectName,
        semester=subject.semester,
        year=subject.year,
    )

    # Decrease the available seats by 1
    subject.seatAvailable -= 1

    # Update status to 'Close' if no seats are available
    if subject.seatAvailable == 0:
        subject.status = 'Close'

    subject.save()  # Save the updated subject instance to the database

    messages.success(request, f"Subject {subject.subjectCode} has been added to your quota.")
    return redirect('my_quota')


@transaction.atomic
def del_subject(request, id):
    # Get the user's registerSubject entry
    user_subject = get_object_or_404(registerSubject, username=request.user.username, subjectCode=id)

    # Get the corresponding subject to update seat availability
    subject = get_object_or_404(Subject, subjectCode=id)

    # Delete the user's subject entry
    user_subject.delete()

    # Increase the seat available by 1
    subject.seatAvailable += 1

    # Update status to 'Open' if seats become available
    if subject.seatAvailable > 0:
        subject.status = 'Open'

    subject.save()  # Save the updated subject instance to the database

    messages.success(request, f"Subject {subject.subjectCode} has been removed from your quota.")
    return redirect('my_quota')

