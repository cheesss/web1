from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index),
    #url이 blog/로 끝나면 view.py 파일의 index함수를 실행해준다.
    
    path('', views.PostList.as_view()),
    #cbv방식 

    # path('<int:pk>/',views.single_post_page),
    #int:pk는 정수 pk값을 전달 받은후, single_post_page에 넘겨준다는 뜻

    path('<int:pk>/', views.PostDetail.as_view())

]