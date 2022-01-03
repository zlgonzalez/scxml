#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, task
import subprocess as sp

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "rtsim"
default_task = "publish"

@init
def set_properties(project):
    pass

@task
def generate_py():
    sp.call(["generateDS", "-o", "src/main/python/scxmlgen/scxml.py", "-s",
            "src/main/python/scxmlgen/scxml_app.py", "../xsd/scxml.xsd"])
