from django.urls import path
#from . import views ( views.list 이렇게 써야 함)
from .views import * #(list 이렇게 접근 가능함)

# 2차 url
app_name = 'bookmark'
# app_name 은 template 등에서 쉽게 접근하기 위해 사용한다. ex) bookmark:detail
urlpatterns=[
    #path('url pattern', view, name)
    # name은 name으로 url pattern을 찾는다.
    # 함수형 View 는 함수 이름만, Class View 는 ClassName.as_view()
    #path('', list, name='list'),
    path('', BookmarkListView.as_view(), name="list"),
    path('create/', BookmarkCreateView.as_view(), name='create'),
    # <1:2> 1: data type, 2: data name, 1번은 빠져도 되지만 2번은 빠지면 안된다.
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    # path 와 repath가 구분되어졌다.
    # repath(regexp, , ,) -> 정규표현식으로 쓰기 어려워지면서 나눠짐
]