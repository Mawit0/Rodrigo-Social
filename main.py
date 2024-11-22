class Post:
    def __init__(self):
        self.feed = []  # Queue for post feed (FIFO)
        self.own_posts = []  # Stack for user posts (LIFO)

    def add_post(self, post):
        self.feed.append(post)  # Add to feed (FIFO)
        self.own_posts.append(post)  # Add to own posts (LIFO)

    def display_feed(self):
        return self.feed  # Return all posts in the feed (FIFO)

    def view_own_posts(self):
        return self.own_posts[::-1]  # Return own posts (LIFO)


class Social:
    def __init__(self):
        self.users = []
        self.friends = []
        self.posts = {}  # Dictionary to hold Post objects for each user

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
            for n in self.friends:
                n.append(0)
            self.friends.append([0]*len(self.users))
            self.posts[user] = Post()  # Initialize a Post object for the new user
        return None

    def add_friend(self, user1, user2):
        if user1 in self.users and user2 in self.users:
            i = self.users.index(user1)
            j = self.users.index(user2)
            self.friends[i][j] = 1  
            self.friends[j][i] = 1 
        return None
    
    def show_friends(self, user):
        if user in self.users:
            x = []
            i = self.users.index(user)  

            for j, is_friend in enumerate(self.friends[i]):
                if is_friend == 1:  
                    x.append(self.users[j])  
            print(f"{user}'s friends: {x}")

    def show(self):
        print("  " + "  ".join(self.users))
        for i, n in enumerate(self.friends):
            print(self.users[i], n)

    def add_post(self, user, post):
        if user in self.users:
            self.posts[user].add_post(post)  # Add post to the user's feed and own posts
        return None

    def display_feed(self, user):
        if user in self.users:
            return self.posts[user].display_feed()  # Return the user's feed (FIFO)

    def view_own_posts(self, user):
        if user in self.users:
            return self.posts[user].view_own_posts()  # Return the user's own posts (LIFO)


# Example usage:
social_network = Social()
social_network.add_user("Tito")
social_network.add_user("Teo")
social_network.add_friend("Tito", "Teo")

social_network.add_post("Tito", "Rolen sus ID de Pokemon")
social_network.add_post("Tito", "Hola X UPY Edition")
social_network.add_post("Teo", "Guau")

print(social_network.display_feed("Tito"))  # Display Tito's feed
print(social_network.view_own_posts("Tito"))  # View Tito's own posts
