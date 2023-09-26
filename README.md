# FastAPI OAuth2 Template

This is a template for a FastAPI application with Bearer OAuth2 authentication.

## Description

This FastAPI OAuth2 Template provides a starting point for building web applications with user authentication using OAuth2. It includes endpoints for user registration, token generation, and retrieving user information.

## Features

- User registration
- Token generation
- User information retrieval

## Installation
1. Clone this repository:
```
git clone https://github.com/dffdeeq/fastapi_oauth2_template.git
cd fastapi_oauth2_template
```
2. Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
```
3. Install the dependencies:

```
pip install -r requirements.txt
```
## Usage

Run the FastAPI application:

```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
Replace 0.0.0.0 and 8000 with the desired host and port for your application. 

**Access the FastAPI Swagger documentation at http://localhost:8000/docs to interact with the API and test the endpoints.**

## API Endpoints

### User Registration

- **URL**: `/auth/register`
- **Method**: `POST`
- **Description**: Register a new user.
- **Request Body**:
  - `email` (string): User's email address.
  - `hashed_password` (string): Hashed password for the user.

### Token Generation

- **URL**: `/auth/token`
- **Method**: `POST`
- **Description**: Generate a token for authentication.
- **Request Body**:
  - `username` (string): User's username.
  - `password` (string): User's password.

### Get Current User

- **URL**: `/auth/me`
- **Method**: `GET`
- **Description**: Get information about the currently authenticated user.
- **Response Body**: JSON object containing user information.

## Customization

You can customize this template to fit your project requirements. Make sure to update the following files:

- **src/database.py**: Configure your database connection settings.
- **src/auth/services.py**: Add your authentication logic and customize as needed.
- **src/auth/schemas.py**: Define the data models for users and tokens.

## Dependencies

This project relies on the following Python libraries:

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- dffdeeq
- GitHub: [https://github.com/dffdeeq](https://github.com/dffdeeq)

## Contributing

Contributions are welcome! Please create a pull request with your proposed changes.

## Acknowledgments

- FastAPI community: [https://fastapi.tiangolo.com/community/](https://fastapi.tiangolo.com/community/)

---

Enjoy using this FastAPI OAuth2 Template for your project! If you have any questions or encounter any issues, please don't hesitate to reach out to the author or open an issue on GitHub.
