from django.db import models
from django.forms.models import fields_for_model
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from basic_app.models import Student, School
from django.urls import reverse_lazy


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injected_data'] = 'Injected here'
        return context
    

class SchoolListView(ListView):
    model = School
    context_object_name = 'schools'
    
    
class SchoolDetailView(DetailView):
    model = School
    template_name = 'basic_app/school_detail.html'
    context_object_name = 'school_detail'
    

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = School
    

class SchoolUpdateView(UpdateView):
    model = School
    fields = ('name', 'principal')
    

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('basic_app:list')