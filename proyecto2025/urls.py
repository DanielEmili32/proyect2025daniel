from django.contrib import admin
from django.urls import path, include
from users import urls as users_urls
from users.views import welcome, about
from django.contrib.auth.views import LoginView, LogoutView

# Importar vistas JWT y la vista protegida que crearemos
from rest_framework_simplejwt.views import TokenRefreshView
from users.api_views import (
    MyTokenObtainPairView,
    RegisterView,
    LogoutViewAPI,
    VistaProtegida,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(users_urls)),
    path('',
         LoginView.as_view(template_name="base.html"),
         name="login"
         ),
    path('logout/',
         LogoutView.as_view(),
         name="logout"
         ),
    path('about/', about, name="about" ),

    # --- JWT endpoints ---
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Registro y logout (API)
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/logout/', LogoutViewAPI.as_view(), name='api_logout'),

    # Ruta protegida de ejemplo
    path('api/protegida/', VistaProtegida.as_view(), name='vista_protegida'),
]
