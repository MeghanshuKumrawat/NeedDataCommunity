from django.urls import path
from apps.blogs.views import IndexView, BlogPostListView, BlogPostDetailView, CourseListView, CourseDetailView, WorkshopListView, WorkshopDetailView, contact_us


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blogs', BlogPostListView.as_view(), name='blogpost-list'),
    path('blogs/<int:pk>', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('courses', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('workshops', WorkshopListView.as_view(), name='workshop-list'),
    path('workshops/<int:pk>', WorkshopDetailView.as_view(), name='workshop-detail'),
    path('contact-us', contact_us, name='contact-us'),
]
