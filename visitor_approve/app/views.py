from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Visitor, VisitRequest
from .forms import VisitorForm


def home(request):
    return render(request, 'req_handle.html')


def request_visit(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save()
            visit_request = VisitRequest.objects.create(visitor=visitor, receiver=request.user)
            send_mail(
                'New Visit Request',
                f'You have a new visitor request from {visitor.name}.',
                'naurangilal9675329115@gmail.com',
                [request.user.email],
                fail_silently=False,
            )
            return redirect('visitor_management:success')
    else:
        form = VisitorForm()
    return render(request, 'req_visit.html', {'form': form})


def handle_request(request, request_id, action):
    visit_request = VisitRequest.objects.get(id=request_id)

    if action == 'accept':
        visit_request.status = 'accepted'
    elif action == 'reject':
        visit_request.status = 'rejected'
    elif action == 'wait':
        visit_request.status = 'waiting'

    visit_request.save()
    
    send_mail(
        f'Your Visit Request Status: {visit_request.status.capitalize()}',
        f'Your visit request for {visit_request.visitor.name} has been {visit_request.status}.',
        'naurangilal9675329115@gmail.com',
        [visit_request.visitor.email],
        fail_silently=False,
    )

    return redirect('visitor_management:request_list')



def success(request):
    visitors=Visitor.objects.all()
    return render(request, 'success.html',{'visitors': visitors})


def request_list(request):
    visit_requests = VisitRequest.objects.filter(receiver=request.user)
    return render(request, 'req_list.html', {'visit_requests': visit_requests})

