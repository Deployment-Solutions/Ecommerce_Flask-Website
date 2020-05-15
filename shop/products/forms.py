from wtforms import Form, SubmitField, IntegerField, FloatField, StringField, TextAreaField, validators, BooleanField, TextAreaField, DecimalField, PasswordField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = FloatField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    colour = StringField('Colour', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileAllowed(['jpg','png','gif','jpeg']),'Images only Please'])
    image_2 = FileField('Image 2', validators=[FileAllowed(['jpg','png','gif','jpeg']),'Images only Please'])
    image_3 = FileField('Image 3', validators=[FileAllowed(['jpg','png','gif','jpeg']),'Images only Please'])