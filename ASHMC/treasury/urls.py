from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^$', 'ASHMC.treasury.views.overview', {}, name='fund_overview'),
    # url(r'^overview/$', 'ASHMC.treasury.views.overview', {}, name='fund_overview'),
    url(r'^funds/(?P<fund_name>.*)$', 'ASHMC.treasury.views.ledger', {}, name='ledger'),
    url(r'^clubs/admin', 'ASHMC.treasury.views.club_select', {}, name='club_select'),
    url(r'^clubs/(?P<club_name>.*)/admin$', 'ASHMC.treasury.views.club_admin', {}, name='club_admin'),
    url(r'^clubs/(?P<club_name>.*)/check_request$', 'ASHMC.treasury.views.check_request', {}, name='new_check_request'),
    url(r'^clubs/(?P<club_name>.*)/budget_request$', 'ASHMC.treasury.views.budget_request', {}, name='new_budget_request'),
    url(r'^clubs/(?P<club_name>.*)$', 'ASHMC.treasury.views.club_detail', {}, name='club_detail'),
)