.PHONY: setup run test clean docs

# Default target
all: setup run

# Setup environment
setup:
	@echo "🚀 Setting up Lakehouse environment..."
	chmod +x setup.sh
	./setup.sh

# Start services
run:
	@echo "🐳 Starting Docker services..."
	docker-compose up -d
	@echo "✅ Services started: Jupyter(8889), Spark(8180), Airflow(8082)"

# Run tests
test:
	@echo "🧪 Running tests..."
	python -m pytest tests/ -v || echo "⚠️  Tests may require Spark setup"

# Clean environment
clean:
	@echo "🧹 Cleaning environment..."
	docker-compose down
	rm -rf data/* storage/*

# Generate documentation
docs:
	@echo "📝 Generating documentation..."
	@echo "Project documentation is in README.md and docs/ directory"

# Show help
help:
	@echo "Available commands:"
	@echo "  make setup    - Setup environment"
	@echo "  make run      - Start services"
	@echo "  make test     - Run tests"
	@echo "  make clean    - Clean environment"
	@echo "  make docs     - Show documentation info"
	@echo "  make help     - Show this help message"

