#!/usr/bin/python
#coding:utf-8
"""
WSGI config for spidermanage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from nmaptoolbackground.control import taskcontrol

from dozer import Dozer,Logview
# from spidertool import trace
import faulthandler
import pdb


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spidermanage.settings")

application = get_wsgi_application()
#application = Dozer(application)
# application = Logview(application)
faulthandler.enable()
taskcontrol.scheduleinit()
# pdb.set_trace()


