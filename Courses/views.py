from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from Courses.models import Course


class All_courses(ListView):
    model = Course
    template_name = 'Courses/course_list_view.html'
    context_object_name = 'courses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'All courses'
        return context
