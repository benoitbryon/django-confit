# Makefile for use in django-confit development environment.
# See INSTALL for details about using django-confit as a library.
.PHONY: docs test clean

TOX = tox


test:
	$(TOX)


directories:
	mkdir -p docs/_static
	mkdir -p var/docs


clean:
	find ./ -name "*.pyc" -delete
	find ./ -name "__pycache__" -delete


distclean: clean
	rm -rf *.egg-info


maintainer-clean: distclean
	rm -rf bin/ build/ dist/ include/ lib/ local/ man/ share/
	rm -rf .tox/


test-app:
	$(TOX) -e py27,py33


healthcheck:
	$(TOX) -e healthcheck


test-documentation:
	$(TOX) -e sphinx


sphinx:
	make --directory=docs clean html


documentation: directories sphinx


release:
	fullrelease
