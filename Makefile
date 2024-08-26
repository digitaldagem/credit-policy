DOCKER_IMAGES = $(shell docker images -q credit-policy-src)

up:
	docker-compose up -d --build --remove-orphans

up-local:
	docker-compose up --build --remove-orphans

down:
ifneq ($(strip $(DOCKER_IMAGES)),)
	docker-compose down -v --remove-orphans
	docker rmi $(DOCKER_IMAGES)
endif

.PHONY: up up-local down
