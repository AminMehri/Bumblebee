from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from blog.models import Article

class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ["title", "slug", "description", "thumbnail", "publish","category", "author", "promote", "is_special", "status"]
        elif request.user.is_author:
            self.fields = ["title", "slug", "description", "thumbnail", "publish","category", "is_special", "status"]
        else:
            raise Http404("You son of a b****")
        return super().dispatch(request, *args, **kwargs)
    

class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.promote = False
            if not self.obj.status in ['i', 'd']:
                self.obj.status = 'd'
        return super().form_valid(form)


class AuthorAccessMixin():
    def dispatch(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if article.author == request.user and article.status in ['b', 'd'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You son of a b****")


class AuthorsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect("account:profile")
        else:
            return redirect("login")


class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You son of a b****")