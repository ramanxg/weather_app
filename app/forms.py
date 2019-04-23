from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from findweather import validate_city
from wtforms.validators import DataRequired


class CityForm(FlaskForm):
	city_name = StringField('City', validators=[DataRequired(), validate_city])
	submit = SubmitField('Submit')
