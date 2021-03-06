try:
    from urllib.request import build_opener, Request, HTTPCookieProcessor, \
        URLError, HTTPError
except:
    from urllib2 import build_opener, Request, HTTPCookieProcessor, \
        URLError, HTTPError

try:
    from urllib.parse import urlencode, urljoin, parse_qsl, urlparse, \
        urlencode
except ImportError:
    from urlparse import urljoin, parse_qsl, urlparse
    from urllib import urlencode

try:
    from http.cookiejar import CookieJar, MozillaCookieJar
except ImportError:
    from cookielib import CookieJar, MozillaCookieJar

try:
    from html.parser import HTMLParser
except ImportError:  # Python < 3
    from HTMLParser import HTMLParser
