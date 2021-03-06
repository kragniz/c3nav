from django.conf.urls import url
from django.views.generic import TemplateView

from c3nav.editor.views import edit_mapitem, finalize, list_mapitems, list_mapitemtypes, oauth_callback

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='editor/map.html'), name='editor.index'),
    url(r'^mapitemtypes/(?P<level>[^/]+)/$', list_mapitemtypes, name='editor.mapitemtypes'),
    url(r'^mapitems/(?P<mapitem_type>[^/]+)/list/$', list_mapitems, name='editor.mapitems'),
    url(r'^mapitems/(?P<mapitem_type>[^/]+)/list/(?P<level>[^/]+)/$', list_mapitems, name='editor.mapitems.level'),
    url(r'^mapitems/(?P<mapitem_type>[^/]+)/add/$', edit_mapitem, name='editor.mapitems.add'),
    url(r'^mapitems/(?P<mapitem_type>[^/]+)/edit/(?P<name>[^/]+)/$', edit_mapitem, name='editor.mapitems.edit'),
    url(r'^finalize/$', finalize, name='editor.finalize'),
    url(r'^oauth/(?P<hoster>[^/]+)/callback$', oauth_callback, name='editor.oauth.callback')
]
