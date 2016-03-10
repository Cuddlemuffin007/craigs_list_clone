from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from pkmn_app.models import AccountProfile, Category


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login_view')


class AccountProfileView(DetailView):
    model = AccountProfile
    template_name = 'pkmn_app/account_profile_detail.html'


class UpdateAccountProfileView(UpdateView):
    model = AccountProfile
    template_name = 'pkmn_app/account_profile_form.html'
    fields = ['preferred_cities']

    def get_success_url(self):
        return reverse('account_detail_view', args=(self.request.user.accountprofile.pk,))
