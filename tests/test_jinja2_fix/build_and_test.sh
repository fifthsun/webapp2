#!/bin/bash
# build_and_test.sh

echo "🔧 Building custom webapp2..."
python -m pip install -e .

echo "🧪 Running compatibility test for autoescape==True ..."
python ./tests/test_jinja2_fix/test_jinja2_escape_fix.py

echo "🧪 Running compatibility test for autoescape==False ..."
python ./tests/test_jinja2_fix/test_jinja2_escape_fix.py

echo "🎉 If you see ✅ above, you're golden!"
