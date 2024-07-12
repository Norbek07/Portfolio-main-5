from django.urls import path
from .views import home_view,contact_view,blog_view,BlogDetailView,service_view, services_view,portfolio_view, workers_view, team_view #blog_detail_view

urlpatterns = [
    path('',home_view,name='home-page'),
    path('contact/',contact_view,name='contact-page'),
    path('blogs/',blog_view,name='blog-page'),
    path('blog/<slug:slug>/',BlogDetailView.as_view(),name='blog-detail-page'),
    path('service/',service_view,name='service-page'),
    path('services/',services_view,name='services-page'),
    path('portfolio/',portfolio_view, name='portfolio-page'),
    path('workers/',workers_view,name='workers-page'),
    path('team/',team_view,name='team-page'),
]
