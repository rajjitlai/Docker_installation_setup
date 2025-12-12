# Docker Setup Tutorial - Python Server

This tutorial will guide you through setting up and running a simple Python Flask server using Docker.

## What is Docker?

Docker is a platform that uses containerization technology to package applications and their dependencies into lightweight, portable containers. Think of Docker as a way to create a "shipping container" for your software that works consistently across different environments.

### Key Concepts

#### Containers vs Virtual Machines

**Traditional Virtual Machines (VMs):**
- Each VM includes a full operating system
- Heavy resource usage (CPU, memory, disk)
- Slow to start
- Example: Running Windows inside Linux

**Docker Containers:**
- Share the host operating system kernel
- Lightweight and fast
- Quick to start and stop
- Isolated but efficient

```
┌─────────────────────────────────────┐
│         Virtual Machine              │
│  ┌──────────┐  ┌──────────┐        │
│  │   App    │  │   App    │        │
│  │   OS     │  │   OS     │        │
│  └──────────┘  └──────────┘        │
│      Hypervisor                     │
└─────────────────────────────────────┘
           Host Operating System

┌─────────────────────────────────────┐
│         Docker Containers           │
│  ┌──────────┐  ┌──────────┐        │
│  │   App    │  │   App    │        │
│  └──────────┘  └──────────┘        │
│      Docker Engine                  │
└─────────────────────────────────────┘
           Host Operating System
```

### Core Docker Components

#### 1. **Docker Image**
- A read-only template used to create containers
- Like a blueprint or recipe
- Contains: application code, runtime, libraries, dependencies
- Example: `python:3.11-slim` is a pre-built image with Python

#### 2. **Docker Container**
- A running instance of an image
- Like a running process based on the image
- Isolated from other containers
- Can be started, stopped, and deleted

#### 3. **Dockerfile**
- A text file with instructions to build an image
- Defines what goes into your container
- Steps include: base image, dependencies, code, configuration

#### 4. **Docker Compose**
- Tool for defining and running multi-container applications
- Uses a YAML file (`docker-compose.yml`)
- Simplifies managing multiple containers together

### Why Use Docker?

#### ✅ **Consistency**
- "Works on my machine" → "Works everywhere"
- Same environment in development, testing, and production
- Eliminates environment-specific bugs

#### ✅ **Isolation**
- Each application runs in its own container
- No conflicts between different projects
- Easy to clean up (just delete the container)

#### ✅ **Portability**
- Run the same container on Windows, Mac, Linux
- Deploy to cloud platforms easily (AWS, Azure, Google Cloud)
- Move between servers without reconfiguration

#### ✅ **Efficiency**
- Containers are lightweight (MBs vs GBs for VMs)
- Fast startup times
- Share resources efficiently

#### ✅ **Scalability**
- Easy to run multiple instances
- Scale up or down quickly
- Perfect for microservices architecture

### Real-World Analogy

Think of Docker like shipping containers:

- **Image** = The blueprint/design of a shipping container
- **Container** = An actual shipping container with your goods
- **Dockerfile** = Instructions for building the container
- **Docker Hub** = A warehouse where you can get pre-built containers

Just like shipping containers standardized global trade, Docker containers standardize software deployment.

### Common Use Cases

1. **Development Environments**
   - Quick setup for new team members
   - Consistent development environment
   - Easy to share project setup

2. **Microservices**
   - Each service in its own container
   - Independent scaling and deployment
   - Technology diversity (Python, Node.js, Java in one project)

3. **CI/CD Pipelines**
   - Test applications in isolated environments
   - Consistent build and test processes
   - Easy deployment to production

4. **Legacy Application Modernization**
   - Containerize old applications
   - Run on modern infrastructure
   - Gradual migration path

### Docker Terminology Cheat Sheet

| Term | Description |
|------|-------------|
| **Image** | Blueprint for creating containers |
| **Container** | Running instance of an image |
| **Dockerfile** | Instructions to build an image |
| **Docker Hub** | Public registry of Docker images |
| **Registry** | Storage and distribution system for images |
| **Volume** | Persistent data storage for containers |
| **Network** | Communication between containers |
| **Compose** | Tool for multi-container applications |

### How Docker Works

1. **Build**: Create an image from a Dockerfile
   ```bash
   docker build -t my-app .
   ```

2. **Run**: Start a container from an image
   ```bash
   docker run my-app
   ```

3. **Share**: Push images to a registry (like Docker Hub)
   ```bash
   docker push my-app
   ```

4. **Pull**: Download images from a registry
   ```bash
   docker pull my-app
   ```

### Getting Started

Docker abstracts away the complexity of managing dependencies, system libraries, and configurations. Instead of worrying about "Does this server have Python 3.11?" or "Are the right libraries installed?", you just run:

```bash
docker-compose up
```

And Docker handles everything else!

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Structure](#project-structure)
3. [Understanding the Files](#understanding-the-files)
4. [Building and Running with Docker](#building-and-running-with-docker)
5. [Using Docker Compose](#using-docker-compose)
6. [Common Docker Commands](#common-docker-commands)
7. [Troubleshooting](#troubleshooting)
8. [Next Steps](#next-steps)

## Prerequisites

Before you begin, make sure you have the following installed:

- **Docker Desktop** (for Windows/Mac) or **Docker Engine** (for Linux)
  - Download from: https://www.docker.com/products/docker-desktop
  - Verify installation: `docker --version`
- **Docker Compose** (usually included with Docker Desktop)
  - Verify installation: `docker-compose --version`

## Project Structure

```
Docker_installation_setup/
├── app.py                 # Python Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker image configuration
├── docker-compose.yml    # Docker Compose configuration
├── .dockerignore        # Files to exclude from Docker build
└── guide.md             # This file
```

## Understanding the Files

### app.py
A simple Flask web server with three endpoints:
- `/` - Welcome message
- `/health` - Health check endpoint
- `/info` - Server information

### requirements.txt
Lists Python packages needed for the application (Flask and Werkzeug).

### Dockerfile
Defines how to build the Docker image:
- Uses Python 3.11 slim base image
- Sets up working directory
- Installs dependencies
- Copies application code
- Exposes port 5000
- Runs the application

### docker-compose.yml
Orchestrates the Docker container:
- Builds the image
- Maps port 5000
- Sets environment variables
- Configures networking

### .dockerignore
Prevents unnecessary files from being copied into the Docker image, reducing build time and image size.

## Building and Running with Docker

### Method 1: Using Docker Commands

#### Step 1: Build the Docker Image

```bash
docker build -t python-server:latest .
```

This command:
- `-t python-server:latest` - Tags the image with name "python-server" and version "latest"
- `.` - Uses the current directory as the build context

#### Step 2: Run the Container

```bash
docker run -d -p 5000:5000 --name my-python-server python-server:latest
```

This command:
- `-d` - Runs in detached mode (background)
- `-p 5000:5000` - Maps port 5000 from container to host
- `--name my-python-server` - Names the container
- `python-server:latest` - The image to run

#### Step 3: Test the Server

Open your browser and visit:
- http://localhost:5000
- http://localhost:5000/health
- http://localhost:5000/info

Or use curl:
```bash
curl http://localhost:5000
```

#### Step 4: View Logs

```bash
docker logs my-python-server
```

#### Step 5: Stop and Remove Container

```bash
docker stop my-python-server
docker rm my-python-server
```

### Method 2: Using Docker Compose (Recommended)

#### Step 1: Build and Start

```bash
docker-compose up -d
```

The `-d` flag runs containers in detached mode.

#### Step 2: View Logs

```bash
docker-compose logs -f
```

#### Step 3: Stop Containers

```bash
docker-compose down
```

#### Step 4: Rebuild After Changes

```bash
docker-compose up -d --build
```

## Common Docker Commands

### Image Management

```bash
# List all images
docker images

# Remove an image
docker rmi python-server:latest

# Remove all unused images
docker image prune -a
```

### Container Management

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop <container-name>

# Start a stopped container
docker start <container-name>

# Remove a container
docker rm <container-name>

# Execute a command in a running container
docker exec -it <container-name> /bin/bash
```

### Docker Compose Commands

```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# Stop services
docker-compose stop

# Stop and remove containers
docker-compose down

# View logs
docker-compose logs

# Rebuild images
docker-compose build

# View running services
docker-compose ps
```

## Troubleshooting

### Port Already in Use

If port 5000 is already in use, change the port mapping:

**Docker command:**
```bash
docker run -d -p 8080:5000 --name my-python-server python-server:latest
```
Then access at http://localhost:8080

**Docker Compose:**
Edit `docker-compose.yml` and change:
```yaml
ports:
  - "8080:5000"
```

### Container Won't Start

1. Check logs: `docker logs <container-name>`
2. Verify Dockerfile syntax
3. Ensure requirements.txt is correct
4. Check if port is available

### Permission Issues (Linux)

If you encounter permission errors:
```bash
sudo usermod -aG docker $USER
```
Then log out and log back in.

### Rebuild After Code Changes

After modifying `app.py`:
```bash
docker-compose down
docker-compose up -d --build
```

Or with Docker commands:
```bash
docker stop my-python-server
docker rm my-python-server
docker build -t python-server:latest .
docker run -d -p 5000:5000 --name my-python-server python-server:latest
```

## Next Steps

### Development with Hot Reload

To enable hot-reload during development, uncomment the volumes section in `docker-compose.yml`:

```yaml
volumes:
  - .:/app
```

And install Flask in development mode with:
```bash
pip install flask[dev]
```

### Adding More Services

You can extend `docker-compose.yml` to include:
- Databases (PostgreSQL, MySQL, MongoDB)
- Redis for caching
- Nginx as a reverse proxy
- Multiple Python services

### Production Considerations

1. **Use specific Python version** instead of `latest`
2. **Multi-stage builds** to reduce image size
3. **Non-root user** for security
4. **Health checks** in docker-compose.yml
5. **Environment-specific configs** using `.env` files
6. **Resource limits** (CPU, memory)

### Example Production Dockerfile

```dockerfile
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
COPY --from=builder /root/.local /home/appuser/.local
COPY --chown=appuser:appuser app.py .
USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH
EXPOSE 5000
CMD ["python", "app.py"]
```

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Best Practices for Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

## Summary

You've successfully learned how to:
- ✅ Create a Python Flask application
- ✅ Containerize it with Docker
- ✅ Build and run Docker containers
- ✅ Use Docker Compose for orchestration
- ✅ Manage Docker images and containers

Happy containerizing! 🐳

