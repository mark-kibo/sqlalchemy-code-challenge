# Restaurant Review Domain Project

This project is focused on creating a restaurant review domain with three main models: `Restaurant`, `Review`, and `Customer`. It leverages SQLAlchemy for database management and provides various methods to interact with the data.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Methods](#methods)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with this project, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/mark-kibo/sqlalchemy-code-challenge.git
   ```

2. Install the project's dependencies using Pipenv:

   ```shell
   cd restaurant-review-domain
   pipenv install
   ```

3. Set up your database by running the migrations:

   ```shell
   pipenv run python manage.py db upgrade
   ```

4. You can now run the project:

   ```shell
   pipenv run python app.py
   ```

## Usage

To use this project, you can interact with it programmatically by creating instances of `Restaurant`, `Review`, and `Customer` and then using the provided methods.

```python
# Example usage
from your_module_name import Restaurant, Review, Customer

# Create instances and perform actions here
```

## Models

### Restaurant

- `id`: Integer, primary key
- `name`: String(50), nullable
- `price`: Integer, nullable
- `reviews`: One-to-many relationship with `Review`
- `customers`: Many-to-many relationship with `Customer`

### Review

- `id`: Integer, primary key
- `rating`: Integer
- `customer_id`: Integer, foreign key referencing `Customer`
- `restaurant_id`: Integer, foreign key referencing `Restaurant`
- `customer`: Many-to-one relationship with `Customer`
- `restaurant`: Many-to-one relationship with `Restaurant`

### Customer

- `id`: Integer, primary key
- `first_name`: String(20)
- `last_name`: String(20)
- `reviews`: One-to-many relationship with `Review`
- `restaurants`: Many-to-many relationship with `Restaurant`

## Methods

Here are some of the key methods available in this project:

- `Customer.get_reviews()`: Get all reviews by a customer.
- `Customer.get_restaurants()`: Get all restaurants reviewed by a customer.
- `Customer.full_name()`: Get the full name of a customer.
- `Customer.favorite_restaurant()`: Get the customer's favorite restaurant.
- `Customer.add_review(restaurant, rating)`: Add a review for a restaurant.
- `Customer.delete_reviews(restaurant)`: Delete all reviews by a customer for a specific restaurant.
- `Review.full_review()`: Get a formatted string for a review.
- `Restaurant.fanciest()`: Get the restaurant with the highest price.
- `Restaurant.all_reviews()`: Get a list of formatted review strings for all reviews of a restaurant.

## Contributing

Contributions to this project are welcome. Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
```

Customize the above template with your project-specific information, such as the actual repository URL, module name, and any additional instructions or details about your project.
