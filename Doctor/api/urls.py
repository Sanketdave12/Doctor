from django.urls import path
from .views.common_views import ContactView, SubscribeView, GetSubscribe
from .views.blog_views import AddBlog
urlpatterns = [
    path('add-contact/', ContactView.as_view(), name='add-contact'),
    path('add-blog/', AddBlog.as_view(), name="add-blog"),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('get-subscribe/', GetSubscribe.as_view(), name='get-subscribe'),

]
