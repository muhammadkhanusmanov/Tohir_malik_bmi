# Tohir_malik_bmi

### Endpoints

#### 1. Admin Login
- **Endpoint:** `/admin/login/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
      "username": "your_username",
      "password": "your_password"
  }
  ```
- **Response:**
  - **Success (200):**
    ```json
    {
        "token": "your_token"
    }
    ```
  - **Error (401):**
    ```json
    {
        "error": "Noto'g'ri login yoki parol"
    }
    ```

#### 2. Create Reservation
- **Endpoint:** `/reserve/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
      "place": 1,
      "full_name": "Ali Valiyev",
      "phone_number": "+998901234567",
      "date": "2025-04-26",
      "start_time": "18:00",
      "end_time": "20:00",
      "order_items": [
          {"dish": 1, "quantity": 2},
          {"dish": 2, "quantity": 1}
      ]
  }
  ```
- **Response:**
  - **Success (201):**
    ```json
    {
        "id": 1,
        "place": 1,
        "full_name": "Ali Valiyev",
        "phone_number": "+998901234567",
        "date": "2025-04-26",
        "start_time": "18:00",
        "end_time": "20:00",
        "order_items": [
            {"dish": 1, "quantity": 2},
            {"dish": 2, "quantity": 1}
        ]
    }
    ```
  - **Error (400):**
    ```json
    {
        "error": "Bu vaqtda bu joy allaqachon band qilingan.",
        "conflicting_reservations": [
            {"full_name": "John Doe", "start_time": "18:00", "end_time": "20:00"},
            ...
        ]
    }
    ```

#### 3. Create Place
- **Endpoint:** `/admin/places/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
      "name": "New Restaurant",
      "capacity": 50,
      "description": "A cozy place for family gatherings.",
      "extra": "Additional information about the place.",
      "image_url": "http://example.com/image.jpg",
      "hourly_rate": 100.00
  }
  ```
- **Response:**
  - **Success (201):**
    ```json
    {
        "id": 1,
        "name": "New Restaurant",
        "capacity": 50,
        "description": "A cozy place for family gatherings.",
        "extra": "Additional information about the place.",
        "image_url": "http://example.com/image.jpg",
        "hourly_rate": "100.00"
    }
    ```
  - **Error (400):**
    ```json
    {
        "error": "Invalid data provided."
    }
    ```

#### 4. Create Dish
- **Endpoint:** `/admin/dishes/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
      "name": "Pasta",
      "category": "main",
      "price": 12.99,
      "description": "Delicious pasta with tomato sauce.",
      "image": "http://example.com/image.jpg",
      "image_url": "http://example.com/image.jpg"
  }
  ```
- **Response:**
  - **Success (201):**
    ```json
    {
        "id": 1,
        "name": "Pasta",
        "category": "main",
        "price": 12.99,
        "description": "Delicious pasta with tomato sauce.",
        "image": "http://example.com/image.jpg",
        "image_url": "http://example.com/image.jpg"
    }
    ```
  - **Error (400):**
    ```json
    {
        "error": "Invalid data provided."
    }
    ```

#### 5. Admin Reservation List
- **Endpoint:** `/admin/reservations/`
- **Method:** `GET`
- **Response:**
  - **Success (200):**
    ```json
    [
        {
            "id": 1,
            "full_name": "Ali Valiyev",
            "date": "2025-04-26",
            "start_time": "18:00",
            "end_time": "20:00"
        },
        ...
    ]
    ```

#### 6. Confirm Reservation
- **Endpoint:** `/admin/reservations/<int:pk>/confirm/`
- **Method:** `PATCH`
- **Response:**
  - **Success (200):**
    ```json
    {
        "message": "Buyurtma tasdiqlandi."
    }
    ```
  - **Error (404):**
    ```json
    {
        "error": "Buyurtma topilmadi."
    }
    ```

#### 7. Top Dishes
- **Endpoint:** `/admin/stats/top-dishes/`
- **Method:** `GET`
- **Response:**
  - **Success (200):**
    ```json
    [
        {"dish__name": "Dish 1", "total_sold": 10},
        ...
    ]
    ```

#### 8. Peak Times
- **Endpoint:** `/admin/stats/peak-times/`
- **Method:** `GET`
- **Response:**
  - **Success (200):**
    ```json
    [
        {"start_time": "18:00", "count": 5},
        ...
    ]
    ```

### Notes
- Ensure that you have the necessary permissions to access admin endpoints.
- For the `Create Reservation` endpoint, no authentication is required.