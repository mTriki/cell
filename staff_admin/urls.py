from django.conf.urls import patterns, url
from users.views import ListCustomers

urlpatterns = patterns('staff_admin.views',
    url(r'^customers/$', ListCustomers.as_view(), name = 'staff_admin_customers'),
)