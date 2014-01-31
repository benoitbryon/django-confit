#################
Contributor guide
#################


*****************************
Setup development environment
*****************************

Requirements:

* git
* tox

As an example, using virtualenv:

.. code:: sh

   git clone git@github.com:benoitbryon/django-confit.git # Use your fork here!
   cd django-confit/
   virtualenv ./
   source bin/activate
   pip install tox
   make test
