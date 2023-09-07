from django import forms

from repair_service.models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
