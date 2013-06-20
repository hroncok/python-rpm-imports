# this should be called with %{buildroot}%{python_sitelib} as argument
import sys, os, pkgutil, re

# Go to the given directory and add it to sys.path
os.chdir(sys.argv[1])
sys.path = ['.'] + list(filter(lambda x: 'site-packages' not in x, sys.path))

# List all available modules in that directory
for importer, modname, ispkg in pkgutil.walk_packages(path='.'):
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
    print(modname)
