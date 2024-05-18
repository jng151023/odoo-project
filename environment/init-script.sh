#!/bin/sh

echo "--- Odoo Environment Init ---"
echo "Creating needed folders..."
mkdir -p ./data/odoo/config
mkdir -p ./data/odoo/data
mkdir -p ./data/odoo/addons
mkdir -p ./data/postgres
echo "Done. Now you can start docker compose!"