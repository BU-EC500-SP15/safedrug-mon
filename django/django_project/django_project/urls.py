from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from website import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name = 'index'),
    url(r'^wordcloud/', views.wordcloud, name = 'wordcloud'),
    url(r'^result/', views.result, name = 'result'),
    url(r'^bar_result/', views.bar_result, name = 'bar_result'),
    url(r'^admin/', include(admin.site.urls)),
)
