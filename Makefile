export DOCKER_DEFAULT_PLATFORM=linux/amd64

up:
	docker compose -f docker-compose.yml up -d

down:
	docker compose -f docker-compose.yml down --remove-orphans

up_rebuild:
	docker compose -f docker-compose.yml up --build -d
