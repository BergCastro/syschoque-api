from django.urls import path, include

from django.contrib import admin
from rest_framework import routers
from teste_fisico import urls as teste_fisico_urls
from p1.api.viewsets import ControleOficioViewSet
admin.autodiscover()



# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

router = routers.DefaultRouter()
router.register(r'controleoficio', ControleOficioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path("admin/", admin.site.urls),
]

admin.site.site_header = 'SAF'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Seja bem-vindo ao SAF'


