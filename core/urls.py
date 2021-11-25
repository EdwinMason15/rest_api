from django.urls import path
from core import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #path('hello-view/', views.HelloApiView.as_view()),
    path('stores/', views.StoreList.as_view(), name="stores"),
    path('stored/<int:pk>/', views.StoreListDetail.as_view()),
    path('brands/', views.StoreList.as_view()),
    path('deals/', views.StoreList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)