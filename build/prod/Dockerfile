FROM odoo:17

ENV TZ=Asia/Bangkok

USER root

RUN groupadd -g 1000 odoo-data && usermod -aG odoo-data odoo

COPY —chown=odoo:odoo-data ./build/prod/conf/odoo.prod.conf /etc/odoo/odoo.conf

COPY —chown=odoo:odoo-data ./addons /var/lib/odoo/addons/17.0

USER odoo

CMD [ "odoo" ]