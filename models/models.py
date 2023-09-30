# create our classes
from seed.engine import Base, run_migration, session
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, backref



# many many association table

association_table=Table(
    "association",
    Base.metadata,
    Column("customer_id", ForeignKey("customers.id")),
    Column("restaurant_id", ForeignKey("restaurants.id")),
)

class Restaurant(Base):
    __tablename__= "restaurants"


    id = Column(Integer(), primary_key=True)
    name=Column(String(50), nullable=True)
    price=Column(Integer(), nullable=True)

    # relationships
    getreviews=relationship("Review", backref="reviews")
    customers= relationship("Customer", secondary=association_table, back_populates= "restaurants")

    # methods
    def reviews(self):
        return self.reviews
    
    def get_customers(self):
        return self.customers
    
    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        review_strings = []
        for review in self.getreviews:
            review_strings.append(review.full_review())
        return review_strings
    
    
class Review(Base):
    __tablename__= "reviews"


    id = Column(Integer(), primary_key=True)    
    rating=Column(Integer())


    # one to many rel
    customer_id=Column(Integer(), ForeignKey("customers.id"))
    restaurant_id=Column(Integer(), ForeignKey("restaurants.id"))

    def customer(self):
        return session.query(Customer).filter(Customer.id == self.customer_id).first()
    

    def restaurant(self):
        return session.query(Restaurant).filter(Restaurant.id == self.restaurant_id).first()

    def full_review(self):
        return f"Review for {self.restaurant().name} by {self.customer().full_name()}: {self.rating} stars."

class Customer(Base):
    __tablename__= "customers"


    id = Column(Integer(), primary_key=True)
    first_name=Column(String(20))
    last_name=Column(String(20))


    # rel
    reviews=relationship("Review", backref="cust_reviews")
    restaurants= relationship("Restaurant", secondary=association_table, back_populates= "customers")

     # methods
    def get_reviews(self):
        return self.reviews
    
    def get_restaurants(self):
        return self.restaurants
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def favorite_restaurant(self):
        rating=0
        restaurant=None
        for restaurant in self.get_restaurants():
            if restaurant.rating > rating:
                rating = restaurant.rating
                restaurant =restaurant
        return restaurant
    def add_review(self, restaurant, rating):
        session.add(Review(rating=rating, customer_id=self.id, restaurant_id=restaurant.id))
        session.commit()
        return "created"
    
    def delete_reviews(self, restaurant):
        for review in self.reviews:
            if review.restaurant_id == restaurant:
                session.delete(review)
        session.commit()
    


run_migration()