from django.conf.urls.defaults import *

from views import empty_view, LazyRedictView, login_required_view

urlpatterns = patterns('',
    url(r'^redirected_to/$', empty_view, name='named-lazy-url-redirected-to'),
    url(r'^login/$', empty_view, name='some-login-page'),
    url(r'^login_required_view/$', login_required_view),
    url(r'^redirect/$', LazyRedictView.as_view()),
)
