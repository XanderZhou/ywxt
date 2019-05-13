from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username



# class SiteType(db.Model):
#     __tablename__ = 'sitetype'
#     id = db.Column(db.Integer, primary_key=True)
#     site_type = db.Column(db.String(20), unique=True, nullable=False)
#     category = db.relationship('Site',backref=db.backref('sitetype'))
#     def __repr__(self):
#         return  self.site_type


class Site(db.Model):
    __tablename__ = 'site'
    id = db.Column(db.Integer, primary_key=True)
    site_type = db.Column(db.String(20), unique=False, nullable=False)
    site_name = db.Column(db.String(20), unique=True, nullable=False)
    site_url = db.Column(db.String(100), unique=True,nullable=False)
    image = db.Column(db.String(80),nullable=True, default='default.png')
    describe = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<site_name %r>' % self.site_name
