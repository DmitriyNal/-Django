from django.contrib import admin
from django.urls import path

from task1.views import index, IndexView, sign_up_by_htm, sign_up_by_django, home_page, get_auto, pl_news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', index, name='index'),
    path('credit/', IndexView.as_view()),
    path('', home_page, name='home'),
    path('registration/', sign_up_by_htm),
    path('registration2/', sign_up_by_django),
    path('auto/', get_auto),
    path('platform/news/', pl_news, name='news')

]
