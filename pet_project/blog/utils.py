from .models import *
from django.db.models import *

class DataMixin:

    def get_post_content(self):
        context = dict()
        categories = Category.objects.all()
        context['categories'] = categories
        return context
       