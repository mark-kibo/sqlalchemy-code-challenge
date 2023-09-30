from seed.engine import session
from models import Restaurant, Customer

# restaurant=session.query(Customer).first()


# restaurant.get_restaurants()



# # Example usage
# customer = session.query(Customer).first()
# restaurant = session.query(Restaurant).first()

# # Delete all reviews by the customer for a specific restaurant
# customer.delete_reviews(restaurant)

# # Get the fanciest restaurant
# fanciest_restaurant = Restaurant.fanciest()

# # Get all reviews for a restaurant
# reviews = fanciest_restaurant.all_reviews()
# for review in reviews:
#     print(review)


# Create a new customer
new_customer = Customer(first_name="John", last_name="Doe")

# Add the customer to the database
session.add(new_customer)
session.commit()

# Add a review for a restaurant
restaurant = session.query(Restaurant).filter_by(id=1).first()  # Replace 1 with the desired restaurant ID
new_customer.add_review(restaurant, rating=4)

# Retrieve reviews for the customer
customer_reviews = new_customer.get_reviews()
for review in customer_reviews:
    print(f"Review ID: {review.id}, Rating: {review.rating}")

# Get the customer's full name
full_name = new_customer.full_name()
print(f"Customer's Full Name: {full_name}")

# Find the customer's favorite restaurant
favorite_restaurant = new_customer.favorite_restaurant()
if favorite_restaurant:
    print(f"Favorite Restaurant: {favorite_restaurant.name}, Rating: {favorite_restaurant.rating}")
else:
    print("Customer has not reviewed any restaurants yet.")

# Delete reviews for a specific restaurant
restaurant_to_delete_reviews = session.query(Restaurant).filter_by(id=2).first()  # Replace 2 with the desired restaurant ID
new_customer.delete_reviews(restaurant_to_delete_reviews)

# Clean up
session.delete(new_customer)
session.commit()
session.close()
