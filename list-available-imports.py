#!/usr/bin/python
"""
Automatic provides generator for Python modules.

Should be called with %{buildroot}%{python_sitelib} as argument.
"""
# Copyright 2013 Miro Hroncok <mhroncok@redhat.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import sys, os, pkgutil, re

paths = [path.rstrip() for path in sys.stdin.readlines()]

for path in paths:
    if path.endswith('site-packages'):
        # Go to the given directory and add it to sys.path
        os.chdir(path)
        sys.path = ['.'] + list(filter(lambda x: 'site-packages' not in x, sys.path))

        # List all available modules in that directory
        for importer, modname, ispkg in pkgutil.walk_packages(path='.'):
            # if module name starts with 1 underscore, do not print it
            try:
                if modname.split('.')[-1][0] == '_' and modname.split('.')[-1][1] != '_':
                    continue
            except IndexError:
                pass
            # if it is a directory/package, check if it's not just a namespace
            if ispkg:
                try:
                    with open('./'+modname.replace('.','/')+'/__init__.py','r') as f:
                        init_source = f.read()
                    if re.search(r'^[^#]*declare_namespace\s*\(\s*__name__\s*\)',init_source,re.M):
                        continue
                    if re.search(r'^[^#]*extend_path\s*\(\s*__path__\s*,\s*__name__\s*\)',init_source,re.M):
                        continue
                except IOError:
                    pass
            print('python-import('+modname+')')
