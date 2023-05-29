from sqlalchemy import func
from wtforms import SelectField, TextAreaField
from wtforms.validators import DataRequired

from src.admin.base import SecureModelView


class ProductView(SecureModelView):

    create_modal = True
    edit_modal = True
    can_export = True
    column_editable_list = ["name", "description", "price"]

    form_overrides = {"category": SelectField, "description": TextAreaField}
    form_args = {"category": {"validators": [DataRequired()], "choices": ["CPU", "GPU", "RAM", "PSU"]}}
    form_columns = ["name", "description", "category", "price"]

    def get_query(self):
        return self.session.query(self.model).filter(self.model.category != None)

    def get_count_query(self):
        return self.session.query(func.count("*")).filter(self.model.category != None)