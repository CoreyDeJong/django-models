from django.urls import path
from .views import HomeView, PostDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('blog/', PostPageView.as_view(), name='blog'),
    path('blog_details/<int:pk>', PostDetailsView.as_view(), name='blog_details'),

]