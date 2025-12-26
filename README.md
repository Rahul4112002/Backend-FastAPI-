# Backend FastAPI Project

A robust and scalable FastAPI backend application with modern Python best practices.

## Features

- **FastAPI Framework**: High-performance async web framework
- **RESTful API**: Well-structured REST endpoints
- **Authentication**: JWT-based authentication system
- **Database Integration**: SQLAlchemy ORM with PostgreSQL support
- **Migration Support**: Alembic for database migrations
- **Async Operations**: Built-in async/await support
- **API Documentation**: Auto-generated Swagger/OpenAPI docs
- **Testing**: Pytest integration for comprehensive testing

## Tech Stack

- **Framework**: FastAPI 0.115+
- **Server**: Uvicorn with websocket support
- **Database**: PostgreSQL with SQLAlchemy 2.0
- **Authentication**: JWT with python-jose
- **Validation**: Pydantic v2
- **Task Queue**: Celery with Redis
- **Testing**: Pytest with async support

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Rahul4112002/Backend-FastAPI-.git
cd Backend-FastAPI-
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run database migrations:
```bash
alembic upgrade head
```

## Running the Application

### Development Mode
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## API Documentation

Once running, access the interactive API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

Run tests with pytest:
```bash
pytest

# With coverage
pytest --cov=app tests/
```

## Project Structure

```
.
├── app/
│   ├── api/
│   │   └── routes/
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   └── database.py
│   ├── models/
│   └── schemas/
├── tests/
├── alembic/
├── .env.example
├── .gitignore
├── requirements.txt
└── main.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Author

**Rahul Chauhan**
- GitHub: [@Rahul4112002](https://github.com/Rahul4112002)

## Acknowledgments

- FastAPI documentation and community
- SQLAlchemy for robust ORM support
- Pydantic for data validation