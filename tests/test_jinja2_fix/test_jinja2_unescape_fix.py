#!/usr/bin/env python
# test_jinja2_fix.py

import webapp2
from webapp2_extras import jinja2

# Test basic functionality
app = webapp2.WSGIApplication([])
j2 = jinja2.Jinja2(app)

# Test template rendering
try:
    template_str = j2.environment.from_string("Hello {{ name }}!")
    result = template_str.render(name="webapp2 3.x")
    print(f"✅ Success: {result}") # noqa

    # Test autoescape
    template_str = j2.environment.from_string("Hello {{ name }}!")
    result = template_str.render(name="<script>alert('xss')</script>")
    print(f"✅ Autoescape test: {result}") # noqa

except Exception as e:
    print(f"❌ Error: {e}") # noqa
