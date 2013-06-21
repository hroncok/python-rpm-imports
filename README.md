RPM automatically generated Provides for Python modules
=======================================================

This project aims to extend RPM to automatically list available imports for Python modules, for example:

    Provides: python-import(setuptools.sandbox) = 0.6.36

Status
------

 * The generator somehow works, but needs extended testing
 * Modules using namespaces doesn't work right now
 * If some module throws an unexpected exception, it will break the process (e.g. pyglet.win32)
 * As [RPM Dependency Generator](http://www.rpm.org/wiki/PackagerDocs/DependencyGenerator) ignores my attempts to catch a directory, for each file this scan the entire directory

Requires
--------

At the beginning I also wanted to automatically list dependencies. The problem is I cannot tell if `foo.bar` is a module or a class from this:

    from foo import bar

So right now, I'v dropped this (but you can see the draft in [cde1c06029](https://github.com/hroncok/python-rpm-imports/blob/cde1c06029f6bff27bfe566052e1162ebd45ae25/list-required-imports.py)).

How to test
-----------

Firstly, generate Python 3 files by running `./generate-python3.sh`. Then copy `*.attr` to `/usr/lib/rpm/fileattrs/` and `*.prov` to `/usr/lib/rpm/`. After that `rpmbuild` should generate proper Provides for Python packages.
