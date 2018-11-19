from django.urls import path, include

from django.contrib import admin
from teste_fisico import urls as teste_fisico_urls
admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path('testes/', include(teste_fisico_urls)),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    #path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    #path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path("admin/", admin.site.urls),
]

admin.site.site_header = 'SAF'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Seja bem-vindo ao SAF'


