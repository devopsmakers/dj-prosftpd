=====
Usage
=====

To use Django ProSFTPd in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_prosftpd.apps.DjProSFTPdConfig',
        ...
    )

Add Django ProSFTPd's URL patterns:

.. code-block:: python

    from dj_prosftpd import urls as dj_prosftpd_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_prosftpd_urls)),
        ...
    ]
