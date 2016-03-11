from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView

from pkmn_app.models import AccountProfile, Category, Pokemon, SubCategory


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


class SubCategoryDetailView(DetailView):
    model = SubCategory


class ListingCreateView(CreateView):
    model = Pokemon
    fields = ['name', 'description', 'level', 'image']

    def get_subcategory(self):
        return SubCategory.objects.get(pk=self.kwargs['subcat_id'])

    def form_valid(self, form):
        pokemon_object = form.save(commit=False)
        pokemon_object.trainer = self.request.user
        pokemon_object.categories = self.get_subcategory()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('subcat_list_view', args=(self.kwargs.get('subcat_id'),))


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'pkmn_app/by_category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemon_list'] = Pokemon.objects.filter(categories__category_id=self.kwargs.get('pk'))
        return context

class PokemonDetailView(DetailView):
    model = Pokemon
    template_name = 'pkmn_app/pokemon_detail.html'

