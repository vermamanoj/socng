from django.contrib import admin

from django.contrib import admin
from .models import (Customer, Vertical, Location, Mode)
from .models import (Asset, AssetAction, AssetAttribute, AssetType, AssetFunction, AssetActionOn)

admin.site.register((Customer, Vertical, Location, Mode))
admin.site.register((Asset, AssetAction, AssetAttribute, AssetType, AssetFunction, AssetActionOn))

