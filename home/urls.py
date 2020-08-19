from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.VegetableList.as_view(), name="home"),
    path("fruit/", views.FruitList.as_view(), name="fruit"),
    path("dairy/", views.DairyList.as_view(), name="dairy"),
    path("meat/", views.MeatList.as_view(), name="meat"),
    path("sugar/", views.SugarList.as_view(), name="sugar"),
    path("bread/", views.BreadList.as_view(), name="bread"),
    path("pre-packed/", views.PreList.as_view(), name="pre"),
    path("can/", views.CanList.as_view(), name="can"),
    path("misc/", views.MiscList.as_view(), name="misc"),
    path("item/<str:slug>/", views.ItemList.as_view(), name="item"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
