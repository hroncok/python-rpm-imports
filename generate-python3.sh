#!/usr/bin/env bash
cp python{,3}import.prov
cp python{,3}import.attr
sed -i 's/python/python3/g' python3import.*
sed -i 's/python32/python3/g' python3import.*
