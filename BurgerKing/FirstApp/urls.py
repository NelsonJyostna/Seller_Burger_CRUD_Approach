from .views import *

from django.urls import path

urlpatterns=[

    path('hm/', home, name='hm'),
    path( 'adseller/', addSellerView, name='addseller'),
    path('sseller/', showSellerView, name='showseller'),
    path('useller/<int:id>/', updateSellerView, name='updateseller'),
    path('dseller/<int:id>/', deleteSellerView, name='delseller')
]
