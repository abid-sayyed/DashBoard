from django.urls import path
from .views import MarketViewSet, MarketDetailView


urlpatterns = [
    # Use angle brackets to capture the 'pk' parameter
    path("api/<int:pk>/", MarketDetailView.as_view(), name="market_detail"),
    path("api", MarketViewSet.as_view(), name="market_list"),  # Removed 'pk' from this path
]
