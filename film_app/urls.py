from django.urls import path
from django.conf.urls.static import static
from . import views
from film_project import settings


urlpatterns= [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('addFilm/', views.add_film, name='add_film'),
    path('addDirector/', views.add_director, name='add_director'),
    path('modify_film/<int:id>', views.modify_film, name='modify_film'),
    path('modify_dir/<int:id>', views.modify_dir, name='modify_dir'),
    path('delete_film/<int:id>', views.delete_film, name='delete_film'),
    path('comment_film/<int:id>', views.comment_film, name='comment_film'),
    path('delete_comment/<int:id>', views.delete_comment, name='delete_comment')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
