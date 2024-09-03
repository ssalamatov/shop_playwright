.PHONY: create-image test up

PYTHON=.venv/bin/python
APPNAME=shop_playwright
TESTDIR=./test

create-image:
	docker build -t "${APPNAME}"  -f ./docker/Dockerfile .

test:
	"${PYTHON}" -m pytest "${TESTDIR}"

up:
	docker run -p 2221:2221 -d "${APPNAME}"
