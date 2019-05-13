from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, FileField, SubmitField, SelectField
from wtforms.validators import DataRequired, length, ValidationError
from app.models import Site

class Add_site(FlaskForm):

    site_type = SelectField('类型', choices=[('系统', '系统'), ('网络', '网络'), ('存储', '存储'), ('其它', '其它') ])
    site_name = StringField('名称', validators=[DataRequired(), length(min=2, max=20)])
    site_url = StringField('地址', validators=[DataRequired(), length(min=6,max=100)])
    describe = StringField('描述', validators=[DataRequired(), length(min=0,max=100)])
    image = FileField('图标', validators=[FileRequired()])
    submit = SubmitField('收藏')

    def validate_site_name(self,site_name):
        site_name = Site.query.filter_by(site_name=site_name.data).first()
        if site_name:
            raise ValidationError('网站名称已存在')
    def validate_site_url(self,site_url):
        site_url = Site.query.filter_by(site_url=site_url.data).first()
        if site_url:
            raise ValidationError('网址已存在')