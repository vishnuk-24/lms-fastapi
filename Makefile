.PHONY: help
help:
	@echo "Available targets:"
	@echo "  app.bash             - Run bash shell in app container"
	@echo "  code.format          - Format code using ruff"
	@echo "  code.format.local    - Format code using ruff"

.PHONY: app.bash
django.bash:
	docker compose run --rm app /bin/bash

.PHONY: code.format
code.format:
	@echo "Running code linters and formatters..."
	docker compose run --rm app sh -c "ruff ."

.PHONY: code.format.local
code.format:
	@echo "Running code linters and formatters..."
	ruff .
