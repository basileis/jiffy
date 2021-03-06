from django.conf.urls import patterns, include, url
from modules.engine import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jiffy.views.home', name='home'),
    # url(r'^jiffy/', include('jiffy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # Default landing page for user
    url(r'^$', views.home),
    url(r'^index.html$', views.home),
    url(r'^users', views.users_list),
    url(r'^signup', views.sign_up_user),
    url(r'^confirmUser', views.confirm_user),
    url(r'^invite', views.invite_friends),
    url(r'^referral', views.invited_friends),
    url(r'^faq', views.faq),
    url(r'^t&c', views.terms_and_condition),
)
