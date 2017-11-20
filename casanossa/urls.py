from django.conf.urls import include, url, patterns
from django.contrib import admin

from casaapp.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'casanossa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', home),

]
