from django.urls import include,re_path
from vprofile import views


urlpatterns = [

    re_path(r'create/$',views.createn_new_recode),
    re_path(r'get_all/$',views.get_all_recode),
    re_path(r'^get_one/(?P<_id>[A-Za-z0-9-_]+)',views.get_one_recode),
    re_path(r'^update/(?P<_id>[A-Za-z0-9-_]+)',views.update_recode),
    re_path(r'^delete/(?P<_id>[A-Za-z0-9-_]+)',views.delete_recode),



]