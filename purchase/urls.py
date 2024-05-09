from django.urls import include,re_path
from purchase import views


urlpatterns = [

    re_path(r'purchase_orders/$',views.createn_purchase_orders),
    re_path(r'purchase_orders/$',views.get_all_purchase_orders),
    re_path(r'^purchase_orders/(?P<_id>[A-Za-z0-9-_]+)',views.get_one_purchase_orders),
    re_path(r'^purchase_orders/(?P<_id>[A-Za-z0-9-_]+)',views.update_purchase_orders),
    re_path(r'^purchase_orders/(?P<_id>[A-Za-z0-9-_]+)',views.delete_purchase_orders),

]