from django.contrib import admin
from .models import Client, Order, Post

# Register your models here.
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Post)
