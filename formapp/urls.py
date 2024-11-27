from django.urls import path
from .views import ListClass, FormClass
from . import views

app_name = 'formapp'

urlpatterns = [
    path('list/', ListClass.as_view(), name='list'),  # リスト表示
    path('create/', FormClass.as_view(), name='create'),  # フォーム表示
    path('delete/<int:post_id>',views.delete_form,name='delete')
]
