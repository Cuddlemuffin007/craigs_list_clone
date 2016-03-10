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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from pkmn_app.views import Home, SignUpView, AccountProfileView, UpdateAccountProfileView, \
    SubCategoryDetailView, ListingCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name='home_view'),
    url(r'^login/', auth_views.login, name='login_view'),
    url(r'^logout/', auth_views.logout_then_login, name='logout_view'),
    url(r'^sign_up/', SignUpView.as_view(), name='sign_up_view'),
    url(r'^account_profile/(?P<pk>\d+)',
        login_required(AccountProfileView.as_view()), name='account_detail_view'),
    url(r'^update_account_profile/(?P<pk>\d+)',
        login_required(UpdateAccountProfileView.as_view()), name='update_preferences_view'),
    url(r'^listings/(?P<pk>\d+)', SubCategoryDetailView.as_view(), name='subcat_list_view'),
    url(r'^(?P<subcat_id>\d+)/create/listing/$', ListingCreateView.as_view(), name='listing_create_view')
]
