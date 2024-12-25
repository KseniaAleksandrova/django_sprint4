""" Файл задает основные маршруты (URL) всего проекта. 
Он связывает URL-адреса с представлениями, 
а также определяется как обрабатывать  маршруты в приложении. """

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

""" Основной список маршрутов проекта """
urlpatterns = [
    path('admin/', admin.site.urls), #URL для административной панели
    path('', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/', include('users.urls')),
]
""" Настройка обработчиков ошибок """
handler403 = 'pages.views.csrf_failure' #ошибка 403 (отказ в доступе)

handler404 = 'pages.views.page_not_found' #ошибка 404 (страница не найдена)

handler500 = 'pages.views.internal_error' #ошибка 500 (внутренняя ошибка сервера)

#доп настройка для режима DEBUG
if settings.DEBUG:
    import debug_toolbar
    #добавление к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
#добавление маршрутов для обработки медиа-файлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
