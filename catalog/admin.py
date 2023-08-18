from django.contrib import admin
from .models import Product, Category, HonorCapsInqueries

admin.site.register(Product)  # let django know about the products model
admin.site.register(Category)  # let django know about the category model
admin.site.register(HonorCapsInqueries)  # let dango know about the WRSInqueries model
