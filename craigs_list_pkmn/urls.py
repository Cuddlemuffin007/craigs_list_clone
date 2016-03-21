"""craigs_list_pkmn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from pkmn_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.CategoryListView.as_view(), name='home_view'),
    url(r'^login/', auth_views.login, name='login_view'),
    url(r'^logout/', auth_views.logout_then_login, name='logout_view'),
    url(r'^sign_up/', views.SignUpView.as_view(), name='sign_up_view'),
    url(r'^account_profile/(?P<pk>\d+)',
        login_required(views.AccountProfileView.as_view()), name='account_detail_view'),
    url(r'^update_account_profile/(?P<pk>\d+)',
        login_required(views.UpdateAccountProfileView.as_view()), name='update_preferences_view'),
    url(r'^subcategory/(?P<pk>\d+)/listings/$', views.SubCategoryDetailView.as_view(), name='subcat_list_view'),
    url(r'^(?P<subcat_id>\d+)/create/listing/$',
        login_required(views.ListingCreateView.as_view()), name='listing_create_view'),
    url(r'^category/(?P<pk>\d+)/listings/$', views.CategoryDetailView.as_view(), name='listing_by_cat_view'),
    url(r'^media/(?P<path>.*)', "django.views.static.serve", {"document_root": settings.MEDIA_ROOT}),
    url(r'^pokemon/(?P<pk>\d+)/detail/$', views.PokemonDetailView.as_view(), name='pokemon_detail_view'),
    url(r'^subcategory/(?P<pk>\d+)/gallery/$', views.SubCategoryGalleryView.as_view(), name='subcat_gallery_view'),
    url(r'^subcategory/(?P<pk>\d+)/thumb/$', views.SubCategoryThumbnailView.as_view(), name='subcat_thumb_view'),
    url(r'^api/categories/$', views.CategoryListAPIView.as_view(), name='category_list_api_view'),
    url(r'^api/categories/(?P<pk>\d+)/pokemon/$',
        views.CategoryPokemonListAPIView.as_view(), name='category_poke_list_api_view'),
    url(r'^api/subcategories/$', views.SubCategoryListAPIView.as_view(), name='subcat_list_api_view'),
    url(r'^api/subcategories/(?P<pk>\d+)/pokemon/$',
        views.SubCategoryPokemonListAPIView.as_view(), name='subcat_poke_list_api_view'),
    url(r'^api/pokemon/$', views.PokemonCreateAPIView.as_view(), name='pokemon_create_api_view'),
    url(r'^api/pokemon/(?P<pk>\d+)/$', views.PokemonRetrieveAPIView.as_view(), name='poke_detail_api_view'),
    url(r'^api/pokemon/(?P<pk>\d+)/update/$', views.PokemonRetrieveUpdateAPIView.as_view(), name='poke_update_api_view')
]
