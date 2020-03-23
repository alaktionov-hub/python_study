"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import app.views as cls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', cls.Login.as_view(), name='login'),
    path('logout/', cls.Logout.as_view(), name='logout'),
    path('registration/', cls.Registration.as_view(), name='registration'),
    path('products_list/', cls.ProductListView.as_view(), name='products_list'),
    path('product_create/', cls.ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', cls.ProductUpdateView.as_view(), name='product_update'),
    path('purchase_create/', cls.PurchaseCreateView.as_view(), name='purchase_create'),
    path('purchase_update/<int:pk>/', cls.PurchaseUpdateView.as_view(), name='purchase_update'),
    path('purchase_return/', cls.PurchaseReturnListView.as_view(), name='purchase_return'),
    path('purchase_deleted/', cls.PurchaseReturnedListView.as_view(), name='purchase_deleted'),
    path('purchase_deleting/<int:pk>/', cls.PurchaseReturnUpdateView.as_view(), name='purchase_deleting'),
    path('basket/', cls.PurchaseListView.as_view(), name='basket'),
    path('', cls.Index.as_view(), name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
