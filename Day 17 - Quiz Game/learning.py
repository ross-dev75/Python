class User:

    def __init__(self, username, user_id):
        print("new user being created")
        self.username = username
        self.user_id = user_id
        self.followers = 0 # default value, not asked for when creating users - think new Instagram account
        self.following = 0

    def follow(self, user): #a method, unlike a function, always needs a 'self' parameter
        user.followers += 1
        self.following += 1
        # the self keyword refers to the object created from the class inside the class blueprint

user_1 = User("Ryan", "001")
user_2 = User("Lily", "002")

print(user_1.username)
print(user_2.user_id)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)