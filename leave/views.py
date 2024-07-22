from django.shortcuts import render,redirect
from .form import CreateLeaveForm, LeaveAdminResponseForm
from django.contrib import messages
from .models import Leave
from django.contrib.auth.decorators import login_required

# Create your views here.
# create a leave request
@login_required
def create_leave_request(request):
    if request.method == 'POST':
        form = CreateLeaveForm(request.POST)
        if form.is_valid():
           var = form.save(commit=False)
           var.user = request.user
           var.save()
           messages.success(request,'Leave request has been submitted and is under review.')
           return redirect('home')
        else:
            messages.warning(request,'Oops,something went wrong,please try again.')
            return redirect('create-leave-request')
    else:
        form = CreateLeaveForm()
        return render(request,'leave/create_leave.html',{'form':form})

# view all created leave requests
@login_required
def all_leave_requests(request):
    leave = Leave.objects.filter(user =request.user)
    return render(request,'leave/all-leave-requests.html',{'leave':leave})

# leave request queue for admin
def leave_request_queue(request):
    leave = Leave.objects.filter(status = 'Pending')
    return render(request,'leave/leave-request-queue.html',{'leave':leave})

# # approve leave request
# def approve_request(request,pk):
#     leave = Leave.objects.get(pk=pk)
#     leave.status = 'Approve'
#     leave.save()
#     messages.success(request,f'You have approved the leave request for {leave.user}')
#     return redirect('home')

# # deny leave request
# def decline_request(request,pk):
#     leave = Leave.objects.get(pk=pk)
#     leave.status = 'Decline'
#     leave.save()
#     messages.success(request,f'You have declined the leave request for {leave.user}')
#     return redirect('home')

# admin response
def admin_response(request,pk):
    leave = Leave.objects.get(pk =pk)
    if request.method == 'POST':
        form = LeaveAdminResponseForm(request.POST,instance=leave)
        if form.is_valid():
            var = form.save()
            if var.status == 'Approve':
                messages.success(request,f'You have approved the leave request for {var.user}')
                return redirect('home')
            elif var.status == 'Decline':
                messages.success(request,f'You have declined the leave request for {var.user}')
                return redirect('home')
            else:
                return redirect('home')
        else:
            messages.warning(request,'Oops,something went wrong.')
            return redirect('home')
    else:
        form = LeaveAdminResponseForm(instance=leave)
        return render(request,'leave/admin-response.html',{'form':form,'leave':leave})