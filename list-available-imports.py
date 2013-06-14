# this should be called with %{buildroot}%{python_sitelib} as argument
import sys, os, pkgutil

# Go to the given directory and add it to sys.path
os.chdir(sys.argv[1])
sys.path += ['.']

# List all available modules in that directory
for importer, modname, ispkg in pkgutil.walk_packages(path='.'):
    print(modname)
