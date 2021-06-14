from django.shortcuts import redirect, render

from .forms import ArticleForm
from .models import Article

def index(request):
    articles = Article.objects.all()

    return render(request, 'article/index.html', {'articles': articles})

def detail(request):
    article = Article.objects.get(pk=1)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()

            return redirect('detail')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'article/detail.html', {'article': article, 'form': form})