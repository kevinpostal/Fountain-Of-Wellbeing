
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('admin', 'admin@2theleft.la'),
     ('FWB', 'fwb420@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'fwbla'             # Or path to database file if using sqlite3.
DATABASE_USER = 'fwbla'             # Not used with sqlite3.
DATABASE_PASSWORD = 'fwbla420!'         # Not used with sqlite3.

#Email Shit
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply@2theleft.la'
EMAIL_HOST_PASSWORD = 'cuntfuck'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
