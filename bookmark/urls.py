from django.contrib import admin
from django.urls import path, re_path #re_path는

#가져오기 * 는 전부다 가져온다는 말
from .views import *

#url 이름을 가지고 패턴을 찾고자할 때 namespace를 사용하려면 app_name이 필수!
app_name = 'bookmark'

urlpatterns = [
    #path('list/', 뷰, 이름(이 이름으로 list패턴을 찾고 싶을때-id같이 쓸수있다. css에서 찾아서 쓸때처럼)),
    # path('', list, name='list'), #메인페이지로 쓸떄는 'list'에서 list를 지우면 홈으로 list페이지가 설정됨


    # 함수형뷰 : 함수 이름만
    # 클래스형 뷰 : 클래스이름.as_view()
    path('', BookmarkListView.as_view(), name='list'), #메인페이지로 쓸떄는 'list'에서 list를 지우면 홈으로 list페이지가 설정됨
    path('write/', BookmarkCreateView.as_view(), name='write'),
    #<1:2> - 1: data type, 2: data name 1번은 빠져도 되는데 2번은 빠지면 안된다
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),

    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
    # re_path(regexp,,),
    # url(regexp,?,?)
]

