from django import forms
from .models import Leave

class CreateLeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        exclude = ('status','admin_comment','date_created','user')

class LeaveAdminResponseForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields =['status','admin_comment']