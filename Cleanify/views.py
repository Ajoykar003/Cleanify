from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView

from django.core.mail import send_mail, EmailMultiAlternatives


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def feed(request):
    return render(request, 'feedback.html')


def send_gmail(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact no')
        place = request.POST.get('place')
        subject = request.POST.get('subject')

        file = request.FILES['file']
        file1 = request.FILES['file2']
        print(name, subject, contact, place)

        msg = EmailMultiAlternatives(
            "Request for Clean at " + place,
            "Name : " + name + "contact : " + contact + " Place : " + place +
            " Location : " + subject,

            # (file.name, file.read()),
            'cleanifypgec@gmail.com',
            ['souviksingh2@gmail.com'],
        )
        msg.attach(file.name, file.read(), file.content_type)
        msg.attach(file1.name, file1.read(), file1.content_type)
        msg.send()

        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponse('Invalid request')


def send_email(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('message')

    send_mail(
        'Feedback from ' + name,
        subject,
        'cleanifypgec@gmail.com',
        ['souviksingh2@gmail.com'],
        fail_silently=False,
    )

    return HttpResponseRedirect(reverse('feed'))
