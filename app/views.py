from django.shortcuts import render

# Create your views here.
from app.models import * 
from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
class home(TemplateView):
    template_name='app/home.html'


class SchoolList(ListView):
    model=School
    context_object_name='schools'
    #template_name='app/school_list.html'
    #queryset=Schools.objects.filter(name='z.p.h school')
    ordering=['name']

class schooldetail(DetailView):
    model=School
    context_object_name='sc'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'
class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'
class SchoolDelete(DeleteView):
    model=School
    context_object_name='sc'
    success_url=reverse_lazy('SchoolList')