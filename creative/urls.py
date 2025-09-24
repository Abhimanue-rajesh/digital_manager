from django.urls import path

from creative.views import CreativeCreateView, CreativeListView, CreativeUpdateView, CreativeDetailView

urlpatterns = [
    path("list/", CreativeListView.as_view(), name="list_creatives"),
    path("create/", CreativeCreateView.as_view(), name="create_creative"),
    path("<int:pk>/update/", CreativeUpdateView.as_view(), name="update_creative"),
    path("<int:pk>/", CreativeDetailView.as_view(), name="detail_creative"),
]
