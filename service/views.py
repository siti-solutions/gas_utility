# service/views.py
from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required

@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_status', service_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'service/create_request.html', {'form': form})

@login_required
def request_status(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    return render(request, 'service/request_status.html', {'service_request': service_request})

# service/views.py
@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'service/notifications.html', {'notifications': notifications})

# service/views.py
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_dashboard(request):
    requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'service/admin_dashboard.html', {'requests': requests})

# service/views.py
@staff_member_required
def admin_dashboard(request):
    form = ServiceRequestSearchForm(request.GET)
    requests = ServiceRequest.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        status = form.cleaned_data.get('status')
        
        if query:
            requests = requests.filter(description__icontains=query)
        if status and status != 'all':
            requests = requests.filter(status=status)
    
    return render(request, 'service/admin_dashboard.html', {'requests': requests, 'form': form})
