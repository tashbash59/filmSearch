from django.shortcuts import render, redirect, reverse 
from .forms import NumbersForm
from .models import SearchNumbers
import random
from django.http import HttpResponseRedirect


def MainPage(request):
	form = NumbersForm()
	if request.method == 'POST':
		film = str(random.randint(int(request.POST.get('first')),int(request.POST.get('second'))))
		return HttpResponseRedirect("https://www.kinopoisk.ru/film/" +film)
	return render(request, "search/index.html", {"form":form})