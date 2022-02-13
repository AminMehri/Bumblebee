from django.core.paginator import Paginator
from account.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from account.mixins import AuthorAccessMixin
from .models import Article, Category
from django.db.models import Count, Q
from datetime import datetime, timedelta
# Create your views here.


def Home(request, page=1):
    last_month = datetime.today() - timedelta(days=30)
    popular_article = Article.objects.published().annotate(count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by('-count', '-publish')[:5]
    articles_list = Article.objects.published()
    paginator = Paginator(articles_list, 9)
    articles = paginator.get_page(page)
    context = {
        "articles": articles,
        "article": Article.objects.filter(promote=True, status="p").order_by('-publish'),
        "popular_article": popular_article
    }
    return render(request, "home.html", context)


# class ArticleList(ListView):
#     # queryset = Article.objects.published()
#     # context_object_name = "articles"
#     context_object_name = "data"
#     template_name = "blog/article_list.html"
#     # paginate_by = 2

#     def get_queryset(self):
#         myset = {
#             "articles": Article.objects.published(),
#             "article": Article.objects.filter(promote=True, status="p").order_by('-publish')
#         }
#         return myset



def Detail(request, slug):
    article = get_object_or_404(Article, slug=slug, status='p')
    ip_address = request.user.ip_address
    if ip_address not in article.hits.all():
        article.hits.add(ip_address)
    
    context = {
        "article": article
    }
    return render(request, "detail.html", context)



class Preview(AuthorAccessMixin, DetailView):
    template_name = 'detail.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)



def Categories(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list, 6)
    articles = paginator.get_page(page)
    context = {
        "category": category,
        "articles": articles,
    }
    return render(request, "category.html", context)


def authorList(request, username, page=1):
    user = get_object_or_404(User, username=username)
    articles_list = user.articles.published()
    paginator = Paginator(articles_list, 6)
    articles = paginator.get_page(page)
    context = {
        "user": user,
        "articles": articles,
    }
    return render(request, "author_list.html", context)


def Contact(request):
    return render(request, "contact.html")


def About(request):
    return render(request, "about.html")

def allCategories(request, page=1):
    category = Category.objects.filter(status=True)
    paginator = Paginator(category, 6)
    articles = paginator.get_page(page)
    context = {
        "category": category,
        "articles": articles,
    }
    return render(request, "all_category_page.html", context)