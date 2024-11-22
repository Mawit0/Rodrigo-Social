class social:
    def __init__(self):
        self.users=[]
        self.friends=[]

    def add_user(self,user):
        if user not in self.users:
            self.users.append(user)

            for n in self.friends:
                n.append(0)
            self.friends.append([0]*len(self.users))
        return None

    def add_friend(self,user1,user2):
        if user1 in self.users and user2 in self.users:
            i=self.users.index(user1)
            j=self.users.index(user2)
            self.friends[i][j]=1  
            self.friends[j][i]=1 
        return None
    
    def show_friends(self,user):
        if user in self.users:
            x=[]
            i=self.users.index(user)  

            for j,is_friend in enumerate(self.friends[i]):
                if is_friend==1:  
                    x.append(self.users[j])  
            print(f"{user}'s friends: {x}")

    def mutual_friends(self,user1,user2):
        if user1 in self.users and user2 in self.users:
            i=self.users.index(user1)
            j=self.users.index(user2)

            mutual=[self.users[k] for k in range(len(self.users)) if self.friends[i][k]==1 and self.friends[j][k]==1]
            print(f"Mutual friends between '{user1}' and '{user2}': {mutual}")

    def recommend(self,user):
        if user in self.users:
            i=self.users.index(user)
            reco=[]

            for j,is_friend in enumerate(self.friends[i]):
                if is_friend==0 and i!=j:
                    cout=sum(self.friends[i][j] and self.friends[j][k] for k in range(len(self.users)))
                    if cout>0:
                        reco.append((self.users[j],cout))

    def show_all(self):
        print("".join(self.users))

    def show(self):
        print("  "+"  ".join(self.users))
        for i,n in enumerate(self.friends):
            print(self.users[i],n)
