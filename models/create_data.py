from seed.engine import session
from models import Restaurant, Review, Customer
# Create Restaurants
restaurants = [
    Restaurant(name="Restaurant 1", price=3),
    Restaurant(name="Restaurant 2", price=2),
    # Add more restaurants here
]

# Create Customers
customers = [
    Customer(first_name="Customer 1", last_name="Lastname 1"),
    Customer(first_name="Customer 2", last_name="Lastname 2"),
    # Add more customers here
]

# # Create Reviews associated with customers and restaurants
# reviews = [
#     Review(rating=4, customer_id=customers[0], restaurant_id=restaurants[0]),
#     Review(rating=5, customer_id=customers[1], restaurant_id=restaurants[1]),
#     # Add more reviews here
# ]

# Establish the many-to-many relationship between customers and restaurants
# customers[0].restaurants.extend(restaurants)
# customers[1].restaurants.extend(restaurants)

restaurants[0].customers.extend(customers)
restaurants[1].customers.extend(customers)


# Add entries to the session and commit them to the database
# session.add_all(restaurants)
# session.add_all(customers)
# # session.add_all(reviews)
# session.commit()


# customer=session.query(Customer).filter(Customer.first_name == "Customer 1").first()

# restaurant=session.query(Restaurant).filter(Restaurant.name == "Restaurant 1").first()
# customer1=session.query(Customer).filter(Customer.first_name == "Customer 2").first()

# restaurant1=session.query(Restaurant).filter(Restaurant.name == "Restaurant 2").first()

# reviews = [
#     Review(rating=4, customer_id=customer.id, restaurant_id=restaurant.id),
#     Review(rating=5, customer_id=customer1.id, restaurant_id=restaurant1.id),
#     # Add more reviews here
# ]

# session.add_all(reviews)
session.commit()