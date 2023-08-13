export DOCKER_DEFAULT_PLATFORM=linux/amd64

up:
	docker compose -f docker-compose.only_backend_without_db.yml up -d

down:
	docker compose -f docker-compose.only_backend_without_db.yml down --remove-orphans

up_rebuild:
	docker compose -f docker-compose.only_backend_without_db.yml up -d --no-deps --build
