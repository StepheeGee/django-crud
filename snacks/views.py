# snacks/views.py
from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.contrib.messages.views import SuccessMessageMixin



class SnackListView(ListView):
    model = Snack
    template_name = 'snacks/snack_list.html'
    context_object_name = 'snacks'

class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snacks/snack_detail.html'

class SnackCreateForm(forms.ModelForm):
    class Meta:
        model = Snack
        fields = ['name', 'rating', 'critical_description', 'reviewer']



class SnackCreateView(CreateView):
    model = Snack
    template_name = 'snacks/snack_form.html'
    fields = ['name', 'rating', 'critical_description', 'reviewer']

    # This line sets the success URL after successfully creating a Snack
    success_url = reverse_lazy('snacks:snack_list')

    
class SnackUpdateView(UpdateView):
    model = Snack
    template_name = 'snacks/snack_form.html'
    fields = ['name', 'rating', 'critical_description', 'reviewer']

class SnackDeleteView(DeleteView):
    model = Snack
    template_name = 'snacks/snack_confirm_delete.html'
    success_url = reverse_lazy('snacks:snack_list') 
