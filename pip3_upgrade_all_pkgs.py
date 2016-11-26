#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip3 install --upgrade --user " + dist.project_name, shell=True)