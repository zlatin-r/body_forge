from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include("body_forge.common.urls")),
    path('accounts/', include("body_forge.accounts.urls")),
    path('workouts/', include("body_forge.workouts.urls")),
    path('exercises/', include("body_forge.exercises.urls")),
])


urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
