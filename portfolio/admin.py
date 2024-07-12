from django.contrib import admin
from .models import Contact,Category,Blog,Portfolio,Team, PortfolioCategory

# Register your models here.

admin.site.register((Contact,Category,Blog,Portfolio,Team, PortfolioCategory)) 
