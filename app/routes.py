import os
from flask import render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename

from app import app, db 
from app.forms import Add_site
from app.models import Site

@app.route('/')
def index():
    xt = Site.query.filter_by(site_type='系统').all()
    wl = Site.query.filter_by(site_type='网络').all()
    cc = Site.query.filter_by(site_type='存储').all()
    qt = Site.query.filter_by(site_type='其它').all()
    return  render_template('index.html', xt = xt, wl = wl, cc = cc, qt = qt )

@app.route('/add_site', methods=['GET', 'POST'])
def add_site():

    add_site = Add_site()

    if add_site.validate_on_submit():
        site_type = add_site.site_type.data
        site_name = add_site.site_name.data
        print (site_name)
        site_url = add_site.site_url.data
        describe = add_site.describe.data
        image = add_site.image.data
        image_name = secure_filename(image.filename)
        image.save(os.path.join('app', 'static', 'images', image_name))

        site = Site( site_type = site_type, site_name = site_name, site_url = site_url, image =image_name, describe = describe )
        db.session.add(site)
        db.session.commit()
        flash('增加成功!', category='success')
        
    return render_template('add_site.html', add_site = add_site )