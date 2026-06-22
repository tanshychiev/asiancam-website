from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("about.html", views.about, name="about"),
    path("services.html", views.services, name="services"),
    path("clients.html", views.clients, name="clients"),
    path("certificates.html", views.certificates, name="certificates"),
    path("staff.html", views.staff, name="staff"),
    path("contact.html", views.contact, name="contact"),

    path("news/<int:news_id>/", views.news_detail, name="news_detail"),

    path("dashboard/news/", views.dashboard_news_list, name="dashboard_news_list"),
    path("dashboard/news/add/", views.dashboard_news_add, name="dashboard_news_add"),
    path("dashboard/news/<int:news_id>/edit/", views.dashboard_news_edit, name="dashboard_news_edit"),
    path("dashboard/news/<int:news_id>/delete/", views.dashboard_news_delete, name="dashboard_news_delete"),
]