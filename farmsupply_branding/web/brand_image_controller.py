import base64
import functools
import io

try:
    from werkzeug.utils import send_file
except ImportError:
    from odoo.tools._vendor.send_file import send_file

import odoo
import odoo.modules.registry
from odoo import http, _
from odoo.http import request, Response
from odoo.modules import get_resource_path
from odoo.tools.mimetypes import guess_mimetype

class BrandImageController(http.Controller):
    
    @http.route(['/brand_logo.png'], type='http', auth="none", cors="*")
    def brand_logo(self, dbname=None, **kw):
        imgname = 'logo'
        imgext = '.png'
        placeholder = functools.partial(get_resource_path, 'web', 'static', 'img')
        dbname = request.db

        if not dbname:
            response = http.Stream.from_path(placeholder(imgname + imgext)).get_response()
        else:
            try:
                # create an empty registry
                registry = odoo.modules.registry.Registry(dbname)
                with registry.cursor() as cr:
                    brand = int(kw['brand']) if kw and kw.get('brand') else False
                    if brand:
                        cr.execute("""SELECT image, write_date
                                        FROM brand_brand
                                       WHERE id = %s
                                   """, (brand,))
                    row = cr.fetchone()
                    if row and row[0]:
                        image_base64 = base64.b64decode(row[0])
                        image_data = io.BytesIO(image_base64)
                        mimetype = guess_mimetype(image_base64, default='image/png')
                        imgext = '.' + mimetype.split('/')[1]
                        if imgext == '.svg+xml':
                            imgext = '.svg'
                        response = send_file(
                            image_data,
                            request.httprequest.environ,
                            download_name=imgname + imgext,
                            mimetype=mimetype,
                            last_modified=row[1],
                            response_class=Response,
                        )
                    else:
                        response = http.Stream.from_path(placeholder('nologo.png')).get_response()
            except Exception:
                response = http.Stream.from_path(placeholder(imgname + imgext)).get_response()

        return response