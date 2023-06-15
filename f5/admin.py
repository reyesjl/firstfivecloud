from django.contrib import admin

from f5.models import (
    CustomUser, RugbyCamp, CampImage, 
    Tour, TourImage, Article, ArticleImage, 
    Tag, ApparelProduct, ProductImage
) 


admin.site.register(CustomUser)
admin.site.register(RugbyCamp)
admin.site.register(CampImage)
admin.site.register(Tour)
admin.site.register(TourImage)
admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(Tag)
admin.site.register(ApparelProduct)
admin.site.register(ProductImage)