from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

    path("/api/create_user/", views.UserCreate.as_view()),
    path("/api/users/(?P&lt;pk&gt;[0-9]+)/", views.UserDetail.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),