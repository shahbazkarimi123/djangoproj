from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

#change in admin page


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('home.urls')),
    path("base/", include('account.urls')),
    path("account/", include('account.urls')),
    path("product/", include('productApp.urls')),
] + static(settings.MEDIA_URL, documment_root=settings.MEDIA_ROOT)
