from django.contrib import admin
from django.urls import path, include
from profiles.urls import profiles_patterns
from pages.urls import pages_patterns
from messenger.urls import messenger_patterns
from webplayground import settings

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),
    path('admin/', admin.site.urls),

    #Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('profiles/', include(profiles_patterns)),

    # Paths de Messenger
    path('messenger/', include(messenger_patterns)),


]

# custom titles for admin
admin.site.site_header = 'Gestion Web Playground'
admin.site.index_title = 'Panel del Administrador'
admin.site.site_title = 'Gestion Panel'

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)