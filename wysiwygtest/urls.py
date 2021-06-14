from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from article.views import index, detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('detail/', detail, name='detail'),
    path('', index, name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
