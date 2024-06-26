from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed,FileRequired
from wtforms.fields import StringField, PasswordField, RadioField, DateField, SelectField, TextAreaField, SubmitField, EmailField,MultipleFileField,DecimalField,IntegerField
from wtforms.validators import DataRequired, equal_to, length, ValidationError,NumberRange

from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from src.models import Users
    
class LoginForm(FlaskForm):
    username_log = StringField("Username", validators=[DataRequired()])
    password_log = PasswordField("Password", validators=[DataRequired(),
                                                     length(min=7, max=64, message="პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო")])
    submit_log = SubmitField("Log In")
    
 

class RegistrationForm(FlaskForm):
    username_reg = StringField("Username", validators=[DataRequired()])
    email_reg = EmailField("Email", validators=[DataRequired()])
    age = IntegerField("Age",validators=[DataRequired(), NumberRange(min=12, max=100)])
    phone = StringField("Phone",validators=[DataRequired(),length(min=9, max=9)])

    password_reg = PasswordField("Password", validators=[DataRequired(),
                                                     length(min=8, max=64, message="პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო")])

    repeat_password_reg = PasswordField("Password", validators=[DataRequired(),
                                                     length(min=8, max=64, message="პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო")])

    submit_reg = SubmitField("Sign In")

    # def validate_username(self, field):
    #     existing_user = Users.query.filter_by(username=field.data).first()
    #     if existing_user:
    #         raise ValidationError("ეს იუზერნეიმი უკვე გამოყენებულია")

    # def validate_password(self, field):
    #     contains_uppercase = False
    #     contains_lowercase = False
    #     contains_digits = False
    #     contains_symbols = False
    #     for character in field.data:
    #         if character in ascii_uppercase:
    #             contains_uppercase = True

    #         if character in ascii_lowercase:
    #             contains_lowercase = True

    #         if character in digits:
    #             contains_digits = True

    #         if character in punctuation:
    #             contains_symbols = True

    #     if not contains_uppercase:
    #         raise ValidationError("პაროლი უნდა შეიცავდეს დიდ ასოებს")
    #     elif not contains_lowercase:
    #         raise ValidationError("პაროლი უნდა შეიცავდეს პატარა ასოებს")
    #     elif not contains_digits:
    #         raise ValidationError("პაროლი უნდა შეიცავდეს ციფრებს")
    #     elif not contains_symbols:
    #         raise ValidationError("პაროლი უნდა შეიცავდეს სიმბოლოებს")
        
        
class AddProductForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    product_model = StringField('Product Model', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)])
    info = TextAreaField('Product Info', validators=[DataRequired()])
    product_images = MultipleFileField('Product Images', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')
    ])
    submit = SubmitField('Add Product')
         
class EditroductForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    product_model = StringField('Product Model', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)])
    info = StringField('Product Info', validators=[DataRequired()])

    submit = SubmitField('Edit Product')