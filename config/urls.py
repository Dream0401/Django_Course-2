from django.contrib import admin
from django.urls import path
# config 폴더 내의 views.py 파일에서 함수들을 가져옵니다.
from .views import hello_world, hello_world_json
from account_app.views import index



urlpatterns = [
    path('admin/', admin.site.urls),
    # 이제 views.py에 정의된 함수를 사용합니다.
    path('', hello_world),
    path('json/', hello_world_json),
    path('account/', index),
]
