from django.urls import path
from . import views
urlpatterns = [
    path('',views.blgliste,name="bloglist"), # 127.0.0.1:8000/blog/
    path('<int:id>/',views.blgdetay,name="blogdetay"), # 127.0.0.1:8000/blog/1/
    path('yeni/',views.blgyeni,name="blogyeni"), #
    path('duzenle/<int:id>/',views.blgduzenle,name="blogduzenle"), #

]
