# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	SFTPUser,
	SFTPUserKey,
	FileHistory,
	FileValidator,
)


class SFTPUserCreateView(CreateView):

    model = SFTPUser


class SFTPUserDeleteView(DeleteView):

    model = SFTPUser


class SFTPUserDetailView(DetailView):

    model = SFTPUser


class SFTPUserUpdateView(UpdateView):

    model = SFTPUser


class SFTPUserListView(ListView):

    model = SFTPUser


class SFTPUserKeyCreateView(CreateView):

    model = SFTPUserKey


class SFTPUserKeyDeleteView(DeleteView):

    model = SFTPUserKey


class SFTPUserKeyDetailView(DetailView):

    model = SFTPUserKey


class SFTPUserKeyUpdateView(UpdateView):

    model = SFTPUserKey


class SFTPUserKeyListView(ListView):

    model = SFTPUserKey


class FileHistoryCreateView(CreateView):

    model = FileHistory


class FileHistoryDeleteView(DeleteView):

    model = FileHistory


class FileHistoryDetailView(DetailView):

    model = FileHistory


class FileHistoryUpdateView(UpdateView):

    model = FileHistory


class FileHistoryListView(ListView):

    model = FileHistory


class FileValidatorCreateView(CreateView):

    model = FileValidator


class FileValidatorDeleteView(DeleteView):

    model = FileValidator


class FileValidatorDetailView(DetailView):

    model = FileValidator


class FileValidatorUpdateView(UpdateView):

    model = FileValidator


class FileValidatorListView(ListView):

    model = FileValidator

