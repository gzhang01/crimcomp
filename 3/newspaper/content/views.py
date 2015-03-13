# Create your views here.
from django.shortcuts import get_object_or_404, render
from models import Article, Image, Contributor

def home(request):
	articles = Article.objects.all()
	images = Image.objects.all()
	contributors = Contributor.objects.all()
	data = {'articles': articles, 'images': images, 'contributors': contributors}
	return render(request, 'home.html', data)

def get_article(request, article_id):
	article = get_object_or_404(Article, id=article_id)
	data = {'article': article}
	return render(request, 'article.html', data)