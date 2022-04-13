# edit

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'controller:11211',
    },
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

OPENSTACK_HOST = "10.30.100.1"
OPENSTACK_KEYSTONE_URL = "http://10.30.100.1:5000/v3"

TIME_ZONE = "Asia/Jakarta"


#add

OPENSTACK_KEYSTONE_MULTIDOMAIN_SUPPORT = True
OPENSTACK_KEYSTONE_DEFAULT_DOMAIN = 'Default'
