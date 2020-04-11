from config import local

assert local.RUCAPTCHA_KEY
assert local.SITE_KEY
assert local.PAGE_URL

DEBUG = local.DEBUG
RUCAPTCHA_KEY = local.RUCAPTCHA_KEY
SITE_KEY = local.SITE_KEY
PAGE_URL = local.PAGE_URL
SNATCH_URL = "https://students.bmstu.ru/teacher"
DEFAULT_SELECTOR = '#bs-example-navbar-collapse-1 > ul:nth-child(1) > li > a.dropdown-toggle'