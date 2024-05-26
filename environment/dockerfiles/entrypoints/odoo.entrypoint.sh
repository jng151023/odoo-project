#!/bin/bash
tmp_folder="/usr/lib/python3/dist-packages/odoo/addons.tmp"
target_folder="/usr/lib/python3/dist-packages/odoo/addons"

if [ -z "$(ls -A $target_folder)" ]; then
    cp -r $tmp_folder/* $target_folder
fi

exec "$@"
