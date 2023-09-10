from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('repair_service.urls')),
                  path('register/', include('account.urls')),
                  path('cart/', include('cart.urls')),
                  path('order/', include('order.urls')),
                  path('statistics/', include('app_statistics.urls')),
                  path('info/', include('info_service.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
