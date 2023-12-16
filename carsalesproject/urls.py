from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='homepage'),
    path('carBrand/<slug:brand_slug>/', views.home, name='brand_wise'),
    path('profile/', include('profile_appp.urls')),
    path('carModel/', include('carModel.urls'))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
