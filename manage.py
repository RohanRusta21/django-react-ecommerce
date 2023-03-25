import os
import sys
import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str
from six import python_2_unicode_compatible
#from six import python_2_unicode_compatible
from django.utils.encoding import smart_str
django.utils.encoding.smart_text = smart_str

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home.settings.dev")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
