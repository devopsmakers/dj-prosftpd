=============================
Django ProSFTPd
=============================

.. image:: https://badge.fury.io/py/dj-prosftpd.svg
    :target: https://badge.fury.io/py/dj-prosftpd

.. image:: https://travis-ci.org/devopsmakers/dj-prosftpd.svg?branch=master
    :target: https://travis-ci.org/devopsmakers/dj-prosftpd

.. image:: https://codecov.io/gh/devopsmakers/dj-prosftpd/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/devopsmakers/dj-prosftpd

Integrate Django and ProSFTPd with MySQL to provide SFTP services

Documentation
-------------

The full documentation is at https://dj-prosftpd.readthedocs.io.

Quickstart
----------

Install Django ProSFTPd::

    pip install dj-prosftpd

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
