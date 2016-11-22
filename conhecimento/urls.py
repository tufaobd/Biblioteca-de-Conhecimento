from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.lista_avisos, name="index"),
    url(r'^detalhe/(?P<pk>[0-9]+)/$', views.detalhe),
    url(r'^novo_aviso/$', views.novo_aviso),
    url(r'^editar_aviso/(?P<pk>[0-9]+)/editar/$',
        views.novo_aviso, name="novo_aviso"),
    url(r'^novo/new/$', views.novo, name='novo'),
    url(r'^publicacoes/(?P<tema>[0-9]+)/$',
        views.lista_publicacoes, name='lista_publicacoes')
]
