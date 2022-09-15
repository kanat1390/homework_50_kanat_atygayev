from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index_view, create_view, game_view, apply_view

app_name = 'catapp'

urlpatterns = [
    path('', index_view, name='index'),
    path('create/', create_view, name='create'),
    path('game/', game_view, name='game'),
    path('apply/', apply_view, name='apply')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)