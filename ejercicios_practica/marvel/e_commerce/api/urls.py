from django.urls import path
from e_commerce.api.views import *


urlpatterns = [
    path('comic_list/', comic_list_api_view, name='comic_list_api_view'),
    path('comic_retrieve/', comic_retrieve_api_view, name = 'comic_retrieve_api_view'),
    path('comic_create/', comic_create_api_view, name = 'comic_create_api_view'),
    path('comic_list_filtered/', comic_list_filtered_api_view, name = 'comic_list_filtered_api_view'),
    path('comic_update_price/', comic_update_price_api_view, name = 'comic_update_price_api_view'),
]