### Simple User Profile API with Django Rest Framework

This repository demonstrates how to build a user profile API using Django Rest Framework (DRF).  
It highlights the use of `Serializer` and `ModelSerializer` classes, including custom implementations of the `create()` and `update()` methods for tailored object creation and update logic.

#### API Documentation
- Interactive documentation available at:
    - [ReDoc UI](http://127.0.0.1:8000/api/schema/redoc/)
    - [Swagger UI](http://127.0.0.1:8000/api/schema/swagger-ui/#/)

#### Key Features
- **JWT Authentication**: Secure API access using the Simple JWT package.
- **Example Requests**: Sample endpoints and usage provided in the `api.http` file.  
    _Tip: Install the REST Client extension in your code editor for easy testing._
- **API Documentation**: Swagger and ReDoc UIs powered by drf-spectacular.

Feel free to explore and modify the code to enhance your understanding of DRF and JWT authentication.