export DOCKER_DEFAULT_PLATFORM=linux/amd64

up:
	docker compose -f docker-compose.backend_without_db.yml up

down:
	docker compose -f docker-compose.backend_without_db.yml down --remove-orphans

up_rebuild:
	docker compose -f docker-compose.backend_without_db.yml up --no-deps --build

up_frontend:
	docker compose -f docker-compose.frontend.yml up

down_frontend:
	docker compose -f docker-compose.frontend.yml down --remove-orphans

up_rebuild_frontend:
	docker compose -f docker-compose.frontend.yml up --no-deps --build