
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("gestion/", include(("gestion.urls", "gestion"))),
    path("", include(("achat.urls", "achat"))),
    path("auth/", include(("authentication.urls", "auth"))),



]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
