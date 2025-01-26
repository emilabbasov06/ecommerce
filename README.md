## FastAPI Application

### Description
This application is a feature-rich RESTful API built using FastAPI. It serves as the backend for managing CRUD operations on a MySQL database. To enhance flexibility and learning, the API is structured with two main application files:
1. **PyMySQL-based file**: Connects directly to the MySQL database and performs CRUD operations.
2. **SQLAlchemy-based file**: Leverages the SQLAlchemy ORM for advanced and efficient database interactions.

Both implementations are robust, secure, and optimized for integration with frontend applications like the DBBoard dashboard.

### Technologies Used
- FastAPI
- MySQL
- PyMySQL
- SQLAlchemy

### Features
- RESTful API endpoints for CRUD operations.
- Dual database handling techniques: raw SQL with PyMySQL and ORM with SQLAlchemy.
- Integration-ready design for frontend applications.

### Commands
To start the PyMySQL-based API:
```bash
uvicorn api.main:app --reload
```

To start the SQLAlchemy-based API:
```bash
uvicorn api.main_orm:app --reload
```

## --------------------------------------------

## DBBoard Dashboard

### Description
DBBoard is a ReactJS-based dashboard application that seamlessly integrates with the FastAPI backend. It offers user authentication, dynamic routing, and a clean interface for managing tasks and data. This dashboard demonstrates a complete full-stack implementation.

### Technologies Used
- ReactJS
- FastAPI (backend integration)
- LocalStorage (for authentication)

### Features
- User authentication using localStorage.
- Dynamic routing for an enhanced user experience.
- Real-time data management with the FastAPI backend.

### Commands
To run the development server:
```bash
npm run dev
```

To build the application for production:
```bash
npm run build
```

