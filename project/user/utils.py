from django.db.models import Count
from django.core.cache import cache

from SmartHome.models import *

menu = [
]

class DataMixin:
  paginate_by = 2
  
  def get_user_context(self, **kwargs):
    
    user_menu = menu.copy()
    if not self.request.user.is_authenticated:
      user_menu.pop(1)

    # context['menu'] = user_menu

    # return context
