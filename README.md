# Django REST Framework Blog API

A complete Blog API built with Django REST Framework featuring authentication, posts, comments, and likes.

## Features

- JWT Authentication
- CRUD operations for Blog Posts
- Comments system
- Like/Unlike functionality
- User management
- Categories

## API Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| POST | `/api/auth/token/` | Get JWT token | No |
| POST | `/api/auth/token/refresh/` | Refresh token | No |
| GET | `/api/posts/` | List all posts | No |
| POST | `/api/posts/` | Create new post | Yes |
| GET | `/api/posts/{id}/` | Get single post | No |
| POST | `/api/posts/{id}/like/` | Like a post | Yes |
| DELETE | `/api/posts/{id}/like/` | Unlike a post | Yes |

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Bikas-sarumagar/blog-management-api.git
cd blog_project