# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'dj_prosftpd'
urlpatterns = [
    url(
        regex="^SFTPUser/~create/$",
        view=views.SFTPUserCreateView.as_view(),
        name='SFTPUser_create',
    ),
    url(
        regex="^SFTPUser/(?P<pk>\d+)/~delete/$",
        view=views.SFTPUserDeleteView.as_view(),
        name='SFTPUser_delete',
    ),
    url(
        regex="^SFTPUser/(?P<pk>\d+)/$",
        view=views.SFTPUserDetailView.as_view(),
        name='SFTPUser_detail',
    ),
    url(
        regex="^SFTPUser/(?P<pk>\d+)/~update/$",
        view=views.SFTPUserUpdateView.as_view(),
        name='SFTPUser_update',
    ),
    url(
        regex="^SFTPUser/$",
        view=views.SFTPUserListView.as_view(),
        name='SFTPUser_list',
    ),
	url(
        regex="^SFTPUserKey/~create/$",
        view=views.SFTPUserKeyCreateView.as_view(),
        name='SFTPUserKey_create',
    ),
    url(
        regex="^SFTPUserKey/(?P<pk>\d+)/~delete/$",
        view=views.SFTPUserKeyDeleteView.as_view(),
        name='SFTPUserKey_delete',
    ),
    url(
        regex="^SFTPUserKey/(?P<pk>\d+)/$",
        view=views.SFTPUserKeyDetailView.as_view(),
        name='SFTPUserKey_detail',
    ),
    url(
        regex="^SFTPUserKey/(?P<pk>\d+)/~update/$",
        view=views.SFTPUserKeyUpdateView.as_view(),
        name='SFTPUserKey_update',
    ),
    url(
        regex="^SFTPUserKey/$",
        view=views.SFTPUserKeyListView.as_view(),
        name='SFTPUserKey_list',
    ),
	url(
        regex="^FileHistory/~create/$",
        view=views.FileHistoryCreateView.as_view(),
        name='FileHistory_create',
    ),
    url(
        regex="^FileHistory/(?P<pk>\d+)/~delete/$",
        view=views.FileHistoryDeleteView.as_view(),
        name='FileHistory_delete',
    ),
    url(
        regex="^FileHistory/(?P<pk>\d+)/$",
        view=views.FileHistoryDetailView.as_view(),
        name='FileHistory_detail',
    ),
    url(
        regex="^FileHistory/(?P<pk>\d+)/~update/$",
        view=views.FileHistoryUpdateView.as_view(),
        name='FileHistory_update',
    ),
    url(
        regex="^FileHistory/$",
        view=views.FileHistoryListView.as_view(),
        name='FileHistory_list',
    ),
	url(
        regex="^FileValidator/~create/$",
        view=views.FileValidatorCreateView.as_view(),
        name='FileValidator_create',
    ),
    url(
        regex="^FileValidator/(?P<pk>\d+)/~delete/$",
        view=views.FileValidatorDeleteView.as_view(),
        name='FileValidator_delete',
    ),
    url(
        regex="^FileValidator/(?P<pk>\d+)/$",
        view=views.FileValidatorDetailView.as_view(),
        name='FileValidator_detail',
    ),
    url(
        regex="^FileValidator/(?P<pk>\d+)/~update/$",
        view=views.FileValidatorUpdateView.as_view(),
        name='FileValidator_update',
    ),
    url(
        regex="^FileValidator/$",
        view=views.FileValidatorListView.as_view(),
        name='FileValidator_list',
    ),
	]
