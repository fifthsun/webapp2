from __future__ import division

from jinja2.runtime import str_join


name = "template1.html"


def root(context):
    l_message = context.resolve("message")
    if 0:
        yield None
    yield str_join([l_message])


blocks = {}
debug_info = '1=8'
