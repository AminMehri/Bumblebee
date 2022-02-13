from django.urls import path
from .views import Home, Detail, Contact, About, Categories, allCategories, authorList, Preview

app_name = "blog"
urlpatterns = [
    path('', Home, name="home"),
    path('page/<int:page>', Home, name="home"),
    path('contact/', Contact, name="contact"),
    path('about/', About, name="about"),
    path('articles/<slug:slug>', Detail, name="detail"),
    path('preview/<int:pk>', Preview.as_view(), name="preview"),
    path('category/<slug:slug>', Categories, name="category"),
    path('category/<slug:slug>/page/<int:page>', Categories, name="category"),
    path('author/<slug:username>', authorList, name="author"),
    path('author/<slug:username>/page/<int:page>', authorList, name="author"),
    path('categories/', allCategories, name="allcategory"),
    path('categories/page/<int:page>', allCategories, name="allcategory"),
]
