from django.shortcuts import render
from apps.blogs.models import BlogPost, Course, CourseKeyPoint, ContactUs
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator

class IndexView(TemplateView):
    template_name = 'index.html'


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogs/blogpost_list.html'
    context_object_name = 'blogposts'
    ordering = ['-date_created']
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.request.GET.get('tag')
        if tag:
            queryset = queryset.filter(tag=tag)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        paginator = Paginator(self.object_list, self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        
        # Calculate the range of page numbers to display
        num_pages = paginator.num_pages
        current_page = page_obj.number
        start_page = max(1, current_page - 2)
        end_page = min(start_page + 2, num_pages)
        
        # Create a list of page numbers
        page_range = range(start_page, end_page + 1)
        
        context['page_obj'] = page_obj
        context['page_range'] = page_range
        
        return context


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogs/blogpost_detail.html'
    context_object_name = 'blogpost'

    
class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    ordering = ['-date_created']
    
class CourseDetailView(DetailView):
    model = BlogPost
    template_name = 'blogs/blogpost_detail.html'
    context_object_name = 'blogpost'

class WorkshopListView(ListView):
    model = Course
    template_name = 'workshops/workshop_list.html'
    context_object_name = 'workshops'
    ordering = ['-date_created']

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(type='WORKSHOPS')
        return queryset
    
class WorkshopDetailView(DetailView):
    model = Course
    template_name = 'workshops/workshop_detail.html'
    context_object_name = 'workshops'
    ordering = ['-date_created']

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(type='WORKSHOPS')
        return queryset
    
def contact_us(request):
    context = {'message': ''}
    if request.method == 'POST':
        ContactUs.objects.create(name=request.POST['name'],
                                 email=request.POST['email'],
                                 phone=request.POST['phone'],
                                 message=request.POST['message'])
        context['message'] = 'Thank you for contacting us. We will get back to you soon.'
        return render(request, 'contact_us.html', context=context)
    return render(request, 'contact_us.html', context=context)