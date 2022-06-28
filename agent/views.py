from audioop import reverse
from urllib import request
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixins

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
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
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
     