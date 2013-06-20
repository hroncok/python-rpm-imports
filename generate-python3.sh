#!/usr/bin/env bash
cp python{,3}-imports.prov
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' python3-imports.prov
sed -i 's|%{python_sitelib}|%{python3_sitelib}|' python3-imports.prov
