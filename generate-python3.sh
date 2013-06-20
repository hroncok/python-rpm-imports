#!/usr/bin/env bash
cp python{,3}-imports.prov
sed -i 's/python/python3/g' python3-imports.prov
