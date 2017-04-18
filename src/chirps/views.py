from django import forms

from django.forms.utils import ErrorList
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Chirp
# Create your views here.

#Create
class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
	#queryset = Chirp.objects.all()
	form_class = TweetModelForm
	template_name = 'chirps/create_view.html'
	#success_url = reverse_lazy("tweet:detail")
	login_url = '/admin/'
   
#Retrieve

#Update
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Chirp.objects.all()
	form_class = TweetModelForm
	template_name = 'chirps/update_view.html'
	#success_url = "/tweet/"
	

#Delete
class TweetDeleteView(LoginRequiredMixin, DeleteView):
	model = Chirp
	template_name = 'chirps/delete_confirm.html'
	success_url = reverse_lazy("tweet:list")
#List/Search

class TweetDetailView(DetailView):
	#template_name = "chirps/detail_view.html"
	queryset = Chirp.objects.all()
	
class TweetListView(ListView):
	#template_name = "chirps/list_view.html"
	def get_queryset(self, *args, **kwargs):
		qs = Chirp.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query)	|
				Q(user__username__icontains=query)
				)
		return qs

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		context['create_form'] = TweetModelForm()
		context['create_url']= reverse_lazy("tweet:create")
		return context

#If doesnt work change tweet to chirp/chirps
def tweet_detail_view(request, pk=None):
	#obj = Chirp.objects.get(pk=pk) #Get from database
	obj = get_object_or_404(Chirp, pk=pk)
	print(obj)
	context = {
		"object": obj
	}

	return render(request, "chirps/detail_view.html", context)

def tweet_list_view(request):
	querryset = Chirp.objects.all()
	print(querryset)
	for obj in querryset:
		print(obj.content)
	context = {
		"object_list": querryset
	}
	return render(request, "chirps/list_view.html", context)	