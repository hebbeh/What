from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import Alerter.views

# Examples:
# url(r'^$', 'what.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
	url(r'^', include("Alerter.urls",namespace="Alerter")),
    url(r'^admin/', include(admin.site.urls)),
]
