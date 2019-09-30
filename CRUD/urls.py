from django.urls import path, reverse

from . import views

urlpatterns = [
    path(
        'post_detail/<int:pk>',
        views.BlogView.as_view(),
        name='post_detail'
    ),
    
    path(
        '',
        views.HomePageView.as_view(),
        name='home'
    )
]
