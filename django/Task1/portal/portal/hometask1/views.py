from django.shortcuts import render
from django.http import HttpResponse


def users(request):
    return render(request, 'users.html')

def articles_html(request):
	return render(request, 'articles.html')

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def first(request):
    return HttpResponse("Hey! It's your first view!!")

def index(request):
    return HttpResponse("It's index page!!")

def main_article(request):
    return HttpResponse('There will be a list with articles')


def uniq_article(request):
    return HttpResponse('This is uniq answer for uniq value')


def article(request, article_id, name=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_id, "Name of this article is {}".format(
            name) if name else "This is unnamed article"))

#######
#------Patr for User 
#######
def main_users(request):
    return HttpResponse('There will be a list with Users, needed for homework')

def article_archive(request):
    return HttpResponse('This is an test for archive')


def users_id(request, users_id):
    return HttpResponse("ID of this user is {}. ".format(users_id))


