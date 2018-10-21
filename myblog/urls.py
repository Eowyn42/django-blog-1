from django.conf.urls import url, include
from myblog.views import stub_view, list_view, detail_view, UserViewSet, GroupViewSet, CategoryViewSet, PostViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# This is where I expect issues
urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name="blog_detail"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]