help: ## - Получить информацию о командах
	@sed \
		-e '/^[a-zA-Z0-9_\-]*:.*##/!d' \
		-e 's/:.*##\s*/:/' \
		-e 's/^\(.\+\):\(.*\)/$(shell tput setaf 6)\1$(shell tput sgr0):\2/' \
		$(MAKEFILE_LIST) | column -c2 -t -s :

network: ## - Создать общую сеть для сервисов
	docker network create custom_network

run: ## - Запустить docker-compose
	docker-compose -f docker-compose.yaml up --build -d

stop: ## - Уронить docker-compose
	docker-compose -f docker-compose.yaml down

tests: ## - Запустить тесты
	python -m pytest -p no:cacheprovider ugc/tests/src/api/v1/*

clean: ## - Очистить docker
	docker stop $$(docker ps -aq)
	docker rm $$(docker ps -aq)
	docker rmi $$(docker images -q)
