.PHONY: create-image test up linter

PYTHON=.venv/bin/python
APPNAME=shop_playwright
TESTDIR=./test
SRCDIR=./src

create-image:
	docker build -t "${APPNAME}"  -f ./docker/Dockerfile .

test:
	"${PYTHON}" -m pytest "${TESTDIR}"

up:
	docker run -p 2221:2221 -d "${APPNAME}"

linter:
	"${PYTHON}" -m flake8 "${SRCDIR}" "${TESTDIR}"
