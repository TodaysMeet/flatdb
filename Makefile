repo ?= rralcala

APP_NAME=flatdb
.PHONY: build

build: ## Build the container
	python3 setup.py sdist bdist_wheel
	docker build -t $(APP_NAME) .

push: build
	docker tag pkstore $(repo)/$(APP_NAME):latest
	docker push $(repo)/$(APP_NAME):latest
