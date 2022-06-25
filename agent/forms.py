from dataclasses import fields
from pyexpat import model
from django import forms
from leads.models import Agent

class AgentModelForm(forms.ModelForm):
    class Meta:
        model=Agent
        fields = (
            'user',
        )