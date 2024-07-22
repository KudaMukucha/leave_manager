from django.urls import path
from . import views
urlpatterns =[
    path('create-leave-request',views.create_leave_request,name='create-leave-request'),
    path('all-leave-requests',views.all_leave_requests,name='all-leave-requests'),
    path('leave-request-queue',views.leave_request_queue,name='leave-request-queue'),
    path('admin-response/<int:pk>/',views.admin_response, name='admin-response'),
    # path('approve-request/<int:pk>/',views.approve_request,name='approve-request'),
    # path('decline-request/<int:pk>/',views.decline_request,name='decline-request')
]