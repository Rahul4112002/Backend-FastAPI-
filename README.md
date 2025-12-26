# 🚀 FastAPI Complete Learning Repository

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red.svg?style=for-the-badge)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

> A comprehensive, production-ready FastAPI learning repository covering fundamentals to advanced concepts with real-world projects.

## 📚 Table of Contents

- [Overview](#-overview)
- [Learning Path](#-learning-path)
- [Projects](#-projects)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Repository Structure](#-repository-structure)
- [Key Features](#-key-features)
- [Technologies Used](#️-technologies-used)
- [Usage](#-usage)
- [Learning Modules](#-learning-modules)
- [Production Apps](#-production-apps)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [Resources](#-resources)

## 🌟 Overview

This repository is a complete learning path for **FastAPI** - from beginner to advanced topics. It includes 99+ modules covering everything from basic HTTP methods to production deployment, authentication, databases, testing, and microservices architecture.

Perfect for developers who want to:
- 🎯 Master FastAPI from scratch
- 🏗️ Build production-ready REST APIs
- 🔐 Implement authentication & authorization
- 💾 Work with databases (SQLAlchemy, Alembic)
- 🧪 Write comprehensive tests
- 🐳 Containerize applications with Docker
- 🚀 Deploy to production

## 🛤️ Learning Path

### **Beginner (Modules 00-20)**
- FastAPI basics & HTTP methods
- Path & query parameters
- Request/response models with Pydantic
- Validation & error handling
- Cookies, headers & forms

### **Intermediate (Modules 21-50)**
- Database integration (SQLAlchemy)
- Migrations with Alembic
- Routers & file structure
- Middleware & CORS
- Background tasks & WebSockets

### **Advanced (Modules 51-99)**
- Authentication (JWT, OAuth2)
- Role-based access control
- Testing strategies
- Performance optimization
- Docker & deployment
- GraphQL integration
- Microservices patterns

## 🎨 Projects

### 📝 **FastNotes** (3 versions)
A complete notes application with progressive enhancement:
- **V1**: Basic CRUD operations
- **V2**: Enhanced features with authentication
- **V3**: Production-ready with full testing suite

### ✅ **TaskKaro** (3 versions)
Task management system:
- **V1**: Simple task manager
- **V2**: Team collaboration features
- **V3**: Production deployment ready

### 🔤 **TextCasePro**
Text manipulation API with multiple case conversions

### 🌐 **Full-Stack Projects**
- FastAPI + React
- FastAPI + Vue
- FastAPI + Next.js
- FastAPI + Nuxt
- Microservices architecture

## ⚡ Prerequisites

- Python 3.8 or higher
- Basic understanding of Python
- Familiarity with REST APIs
- Git installed

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Rahul4112002/Backend-FastAPI-.git
cd Backend-FastAPI-
```

### 2. Create virtual environment

```bash
# Using venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run any module

```bash
cd 01-FastAPI-Basics-Hello-World
uvicorn main:app --reload
```

Visit `http://localhost:8000/docs` for interactive API documentation.

## 📂 Repository Structure

```
Backend-FastAPI-/
├── 00-Setup-Virtual-Environment/
├── 01-FastAPI-Basics-Hello-World/
├── 02-HTTP-Methods-CRUD/
├── 03-HTTP-Methods-All-Verbs/
├── 04-Path-Parameters-Type-Hints/
├── 05-Route-Order-Matters/
├── ...
├── 33-SQLAlchemy-Engine-Setup/
├── 34-SQLAlchemy-Table-Creation/
├── 35-SQLAlchemy-Relationships/
├── 36-SQLAlchemy-CRUD-Services/
├── 37-Alembic-Migrations-Basics/
├── ...
├── 61-Authentication-Basics/
├── 62-JWT-Tokens/
├── 63-OAuth2-Password-Flow/
├── 64-OAuth2-JWT-Bearer/
├── ...
├── 87-Docker-Basics/
├── 88-Docker-Compose/
├── 93-Deployment-Guide/
├── 94-Production-Setup/
├── ...
├── App-FastNotes-V1/
├── App-FastNotes-V2-Enhanced/
├── App-FastNotes-V3-Production/
├── App-TaskKaro-V1/
├── App-TaskKaro-V2-Enhanced/
├── App-TaskKaro-V3-Production/
├── App-TextCasePro/
├── Project-FastAPI-React-FullStack/
├── Project-FastAPI-Vue-FullStack/
├── Project-FastAPI-Next-FullStack/
├── Project-Microservices/
└── Postman-Collections/
```

## ✨ Key Features

- ✅ **99+ Learning Modules** - Comprehensive coverage of all FastAPI concepts
- 🎯 **Real-World Projects** - Production-ready applications
- 🧪 **Testing Included** - Pytest fixtures, mocking, and coverage
- 🔐 **Security Best Practices** - JWT, OAuth2, password hashing
- 💾 **Database Integration** - SQLAlchemy ORM with Alembic migrations
- 🐳 **Docker Ready** - Containerization examples
- 📚 **Well Documented** - Code comments and explanations
- 🔄 **CRUD Operations** - Complete implementation patterns
- 🌐 **WebSockets** - Real-time communication examples
- 📊 **GraphQL** - Integration examples

## 🛠️ Technologies Used

### Core
- **FastAPI** - Modern web framework
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
- **Python 3.8+**

### Database
- **SQLAlchemy 2.0** - ORM
- **Alembic** - Database migrations
- **PostgreSQL/MySQL/SQLite** - Database options

### Authentication
- **JWT** - JSON Web Tokens
- **OAuth2** - Authentication flows
- **Passlib** - Password hashing
- **Python-Jose** - JWT handling

### Testing
- **Pytest** - Testing framework
- **Coverage.py** - Code coverage
- **HTTPX** - Async HTTP client

### Deployment
- **Docker** - Containerization
- **Docker Compose** - Multi-container apps
- **Gunicorn** - Production WSGI server

### Frontend (Full-Stack Projects)
- **React** - UI library
- **Vue.js** - Progressive framework
- **Next.js** - React framework
- **Nuxt** - Vue framework

## 🚀 Usage

### Running Individual Modules

Each module is self-contained and can be run independently:

```bash
# Navigate to any module
cd 13-Request-Body-Pydantic

# Run the FastAPI server
uvicorn main:app --reload
```

### Running Projects

```bash
# Navigate to project
cd App-FastNotes-V1

# Install dependencies
pip install -r requirements.txt

# Run migrations (if needed)
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

### Using Docker

```bash
# Navigate to project with Docker support
cd App-FastNotes-V3-Production

# Build and run with docker-compose
docker-compose up --build
```

## 📖 Learning Modules

### **Fundamentals (00-12)**
- Virtual environment setup
- Hello World application
- HTTP methods (GET, POST, PUT, DELETE, PATCH)
- Path parameters with type hints
- Route ordering
- Enums for predefined values
- Query parameters
- Status codes
- Validation

### **Request/Response Handling (13-24)**
- Pydantic models
- Request body validation
- Multiple body parameters
- Field validation
- Nested models
- JSON schema examples
- Response models
- Response model exclusion

### **Forms & Files (25-29)**
- Form data handling
- File uploads (single & multiple)
- Combining forms and files

### **Error Handling (30-32)**
- HTTPException
- Custom exception handlers
- Validation error override

### **Database (33-42)**
- SQLAlchemy engine setup
- Table creation
- Relationships (One-to-Many, Many-to-Many)
- CRUD services
- Alembic migrations
- Advanced queries
- Pagination strategies
- Database indexing

### **Application Structure (43-48)**
- APIRouter basics
- Router tags
- Path operations
- Dependencies
- File structure organization
- Modular applications

### **Advanced Features (49-60)**
- Background tasks
- Middleware (CORS, custom)
- Lifespan events
- WebSockets
- Testing with pytest
- Mocking

### **Security & Authentication (61-70)**
- Authentication basics
- JWT tokens
- OAuth2 flows
- Password hashing
- Protected routes
- Role-based access control
- Permissions system

### **Production (71-99)**
- Email sending
- File storage
- Environment variables
- Config management
- Logging
- Docker & Docker Compose
- Deployment guides
- Performance optimization
- Caching strategies
- API versioning
- GraphQL integration

## 🏗️ Production Apps

### **FastNotes Application**

A complete notes management system with three progressive versions:

**Features:**
- User authentication
- CRUD operations on notes
- Tagging system
- Search functionality
- RESTful API design

### **TaskKaro Application**

Task and project management system:

**Features:**
- User management
- Task assignment
- Project organization
- Team collaboration
- Status tracking

### **TextCasePro**

Text manipulation API:

**Features:**
- Multiple case conversions
- Batch processing
- RESTful endpoints

## 🧪 Testing

All projects include comprehensive test suites:

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# View coverage report
open htmlcov/index.html
```

### Test Structure
- Unit tests for individual components
- Integration tests for API endpoints
- Database tests with fixtures
- Authentication tests
- Mocking external dependencies

## 🚀 Deployment

### Using Docker

```bash
# Build image
docker build -t fastapi-app .

# Run container
docker run -p 8000:8000 fastapi-app
```

### Using Docker Compose

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Production Deployment

Refer to modules:
- `93-Deployment-Guide/`
- `94-Production-Setup/`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 Resources

### Official Documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

### Learning Resources
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [OAuth2 Specification](https://oauth.net/2/)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Rahul Kumar**

- GitHub: [@Rahul4112002](https://github.com/Rahul4112002)
- Focus: GenAI Engineer | Full-Stack Development
- Learning: Generative AI, LLMs, Agentic AI

## 🌟 Show Your Support

Give a ⭐️ if this project helped you learn FastAPI!

## 📝 Notes

- Each module contains working code examples
- Projects include detailed documentation
- Postman collections available for API testing
- Docker configurations included for deployment

---

**Happy Learning! 🚀**

*Built with ❤️ by developers, for developers*