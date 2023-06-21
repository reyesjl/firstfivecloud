from django.contrib import admin

from f5.f5models import (
    Article, ArticleImage, Tag,
    Product, ProductImage,
    Camp, CampImage, 
    Tour, TourImage,  
) 

# register article models
admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(Tag)

# register product models
admin.site.register(Product)
admin.site.register(ProductImage)

# register camp models
admin.site.register(Camp)
admin.site.register(CampImage)

# register tour models
admin.site.register(Tour)
admin.site.register(TourImage)

