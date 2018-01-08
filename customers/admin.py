from django.contrib import admin
from .models import (Customer, Vertical, Location, Mode)
from .models import (Asset, AssetAction, AssetAttribute, AssetType, AssetFunction, AssetActionOn, AssetDetail)

admin.site.register((Customer, Vertical, Location, Mode))
admin.site.register((Asset, AssetAction, AssetAttribute, AssetType, AssetFunction, AssetActionOn, AssetDetail))
# admin.site.register(Customer)
# admin.site.register(Vertical)
# admin.site.register(Location)
# admin.site.register(Mode)

# admin.site.register(AssetFunction)
# admin.site.register(AssetActionOn)
# admin.site.register(Asset)
# admin.site.register(AssetAction)
# admin.site.register(AssetType)
# admin.site.register(AssetAttribute)
# admin.site.register(AssetDetail)





