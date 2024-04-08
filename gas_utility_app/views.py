from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_service_request.html', {'form': form})

def request_tracking(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'request_tracking.html', {'service_requests': service_requests})
