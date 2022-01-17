from django.urls import path
from api.views import FetchUUIDAPIView

urlpatterns = [
    path('uuids/', FetchUUIDAPIView.as_view(), name="fetch_uuid")
]
