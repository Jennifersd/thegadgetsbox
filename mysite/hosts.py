from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
	host(r'www', settings.ROOT_URLCONF, name='www'),  # redirect 
    host(r'notchfish', 'notchfish.urls', name='notchfish'),
#    host(r'notchfish', 'notchfish.urls', name='notchfish'), #subdomain
#    host(r'(?!www).*', 'mysite.hostsconf.urls', name='wildcard'),
)

'''
from mysite.hostsconf import urls as redirect_urls
host_patterns = patterns = [
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', redirect_urls, name='wildcard'),
]
'''