FROM odoo:15

# Fix: permission denied to /var/lib/odoo inside container when running on linux host
# Cause: in the host, folder data has owner id 1000 and group id 1000(by default) 
#   but inside the container the owner(odoo) id is 101 and group(odoo) id is 101   
#   that do not have permission on the bind mount folder.
# Solution: add a group with id 1000 inside container and then add odoo user to that group
#   to give it permission on bind mount folder.

USER root

RUN groupadd -g 1000 odoo-data && usermod -aG odoo-data odoo

USER odoo

CMD [ "odoo" ]