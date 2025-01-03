# from django.views.generic import TemplateView
from django.urls import path

# urlpatterns = [
#     path("",TemplateView.as_view(template_name="cards/base.html"),name="home"),
# ]
#Note :  we can used as_view when the view file not have any logic but view a templates , so django give us as_view to do that without any effort . 

from . import views
urlpatterns = [
    path("",views.CardListView.as_view(),name="card-list"),
    path("new",
    views.CardCreateView.as_view(),
    name="card-create"
    ),
    path("edit/<int:pk>",
    views.CardUpdateView.as_view(),
    name="card-update"
    ),
    path(
    "box/<int:box_num>",
    views.BoxView.as_view(),
    name="box"
    )
]