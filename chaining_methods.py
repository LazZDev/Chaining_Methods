# Creating a file with the User class, including the __init__ with all the attributes, parameters and default values.
class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

# Adding the display_info(self) method to the User class
    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")

# Adding the enroll method to the User class
    def enroll(self):
        if (self.is_rewards_member):
            print("User already a member.")
            return self

        self.is_rewards_member = True

        self.gold_card_points = 200

        return self

# Adding the spend_points(self, amount) method
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print("Insufficient points.")
            return self


# Creating a user instance and calling the display_info method
user1 = User("Laz", "Dev", "laz.dev@example.com", 38)
user1.display_info()

# Creating two more instances of the User class
user2 = User("John", "Doe", "john.doe@example.com", 25)

# Having the first user spend 50 points
user1.spend_points(50)
user2.enroll().spend_points(80)

user1.display_info()
user2.display_info()
