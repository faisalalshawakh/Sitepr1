from django.urls import include, path
from sitepr.votacao.migrations import views
# (. significa que importa views da mesma directoria)
urlpatterns = [
     path("", views.index, name="index"),
]