from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, ListView

from .forms import ImageCreateForm
from .models import Image


class AddImageView(CreateView):
    model = Image
    form_class = ImageCreateForm
    template_name = 'create.html'

    def post(self, request, *args, **kwargs):
        post = ImageCreateForm(request.POST, request.FILES)
        if post.is_valid():
            post = post.save(commit=False)
            post.created = request.user
            post.save()
            return redirect('homepage')
        else:
            return redirect('create')


class Search(ListView):

    def get_queryset(self):
        return Image.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super(Search, self).get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context
