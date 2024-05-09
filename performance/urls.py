from django.urls import include,re_path

from performance import views


urlpatterns = [

    re_path(r'^vendor/(?P<_id>])/performance',views.vendor_prefomance),

]