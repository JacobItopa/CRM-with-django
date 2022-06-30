import random
from audioop import reverse
from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixins
from django.core.mail import send_mail



# Create your views here.

class AgentListView(OrganisorAndLoginRequiredMixins, generic.ListView):
    template_name = "agent/agent_list.html"
    context_object_name = 'agents'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentCreateView(OrganisorAndLoginRequiredMixins, generic.CreateView):
    template_name = "agent/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agent:agent-list")

    def form_valid(self, form):
        User = form.save(commit=False)
        User.is_agent = True
        User.is_organisor = False
        User.set_password(f"random.randint(0, 1000000)")
        User.save()
        Agent.objects.create(
            user=User,
            organisation=self.request.user.userprofile
        )
        send_mail(
            subject='You are invited to be an agent',
            message='You were added as an agent in CRM. Please Login to continue',
            from_email='jacob@django.com',
            recipient_list=[User.email]
        )
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganisorAndLoginRequiredMixins, generic.DeleteView):
    template_name = "agent/agent_detail.html"
    context_object_name = 'agent'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentUpdateView(OrganisorAndLoginRequiredMixins, generic.UpdateView):
    template_name = "agent/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agent:agent-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentDeleteView(OrganisorAndLoginRequiredMixins, generic.DeleteView):
    template_name = "agent/agent_delete.html"
    context_object_name = 'agent'

    def get_queryset(self):
        return Agent.objects.all()

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
     