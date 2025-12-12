# Docker Python Server Setup

A simple Python Flask server containerized with Docker, perfect for learning Docker basics and containerization.

## 🐳 What is Docker?

Docker is a platform that packages applications and their dependencies into lightweight, portable containers. Think of it as a "shipping container" for your software that works consistently across different environments.

**Key Benefits:**
- ✅ **Consistency** - Works the same on any machine
- ✅ **Isolation** - Each app runs in its own container
- ✅ **Portability** - Run anywhere (Windows, Mac, Linux, Cloud)
- ✅ **Efficiency** - Lightweight and fast compared to virtual machines

For a detailed explanation of Docker concepts, terminology, and how it works, see the **[What is Docker?](guide.md#what-is-docker)** section in the guide.

## 🚀 Quick Start

### Prerequisites
- Docker Desktop (Windows/Mac) or Docker Engine (Linux)
- Docker Compose (included with Docker Desktop)

### Run with Docker Compose (Recommended)

```bash
docker-compose up -d
```

Visit http://localhost:5000 in your browser.

### Run with Docker Commands

```bash
# Build the image
docker build -t python-server:latest .

# Run the container
docker run -d -p 5000:5000 --name my-python-server python-server:latest
```

## 📁 Project Structure

```
.
├── app.py                 # Python Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker image configuration
├── docker-compose.yml    # Docker Compose configuration
├── .dockerignore        # Files excluded from Docker build
├── guide.md             # Comprehensive Docker tutorial
└── README.md            # This file
```

## 🌐 API Endpoints

- `GET /` - Welcome message and server status
- `GET /health` - Health check endpoint
- `GET /info` - Server information (Python version, hostname, environment)

## 📚 Documentation

For detailed instructions, troubleshooting, and advanced usage, see **[guide.md](guide.md)**.

## 🛠️ Common Commands

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild after changes
docker-compose up -d --build
```

## 🧪 Testing

After starting the server, test the endpoints:

```bash
# Using curl
curl http://localhost:5000
curl http://localhost:5000/health
curl http://localhost:5000/info

# Or visit in browser
http://localhost:5000
```

## 📖 Learn More

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Flask Documentation](https://flask.palletsprojects.com/)

## 📝 License

This is a tutorial project for educational purposes.

