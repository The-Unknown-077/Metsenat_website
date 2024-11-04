from app import views
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Metsenat API",
      default_version='v1',
      description="This is Usmons Back-end Metsenat Project API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAdminUser,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # sponsor
    path('sponsor-create/', views.SponsorCreateAPIView.as_view()),
    path('sponsor-list/', views.SponsorListAPIView.as_view()),
    path('sponsor-list/<int:pk>/', views.SponsorDetailAPIView.as_view()),

    # student
    path('student-sponsor-create/', views.CreateStudentSponsorAPIView.as_view()),

    # Statistics
    path('statistic-numbers/', views.StatisticNumberAPIView.as_view()),
    path('graph/', views.GraphAPIView.as_view()),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]














