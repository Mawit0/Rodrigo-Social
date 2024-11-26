class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserta un valor en el BST."""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = TreeNode(value)
        elif value > node.value:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = TreeNode(value)

    def in_order_traversal(self):
        """Realiza un recorrido in-order y devuelve una lista de valores."""
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.value)
            self._in_order_traversal(node.right, result)

    def search(self, value):
        """Busca un valor en el BST."""
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)


class Post:
    def __init__(self):
        self.feed = []  # Queue para el feed general (FIFO)
        self.own_posts = []  # Stack para publicaciones propias (LIFO)

    def add_post(self, post):
        """Agrega una publicación al feed y a las publicaciones propias."""
        self.feed.append(post)  # Agregar al feed (FIFO)
        self.own_posts.append(post)  # Agregar al stack de publicaciones propias (LIFO)

    def display_feed(self):
        """Muestra el feed en orden FIFO."""
        return self.feed

    def view_own_posts(self):
        """Muestra las publicaciones propias en orden LIFO."""
        return self.own_posts[::-1]


class Social:
    def __init__(self):
        self.users = set()  # Conjunto para usuarios (sin duplicados)
        self.friends = {}  # Hash map: {usuario: BST(amigos)}
        self.posts = {}  # Hash map: {usuario: objeto Post}

    def add_user(self, user):
        if user not in self.users:
            self.users.add(user)  # Agregar usuario al conjunto
            self.friends[user] = BST()  # Inicializar BST de amigos
            self.posts[user] = Post()  # Crear objeto Post para el usuario

    def add_friend(self, user1, user2):
        """Agrega una relación de amistad entre dos usuarios."""
        if user1 in self.users and user2 in self.users:
            self.friends[user1].insert(user2)  # Insertar user2 en el BST de user1
            self.friends[user2].insert(user1)  # Insertar user1 en el BST de user2

    def show_friends(self, user):
        """Muestra los amigos de un usuario."""
        if user in self.users:
            friends = self.friends[user].in_order_traversal()  # Recorrido in-order del BST
            print(f"{user}'s friends: {friends}")

    def add_post(self, user, post):
        """Agrega una publicación de un usuario."""
        if user in self.users:
            self.posts[user].add_post(post)  # Agregar publicación al usuario

    def display_feed(self, user):
        """Muestra el feed de un usuario."""
        if user in self.users:
            return self.posts[user].display_feed()

    def view_own_posts(self, user):
        """Muestra las publicaciones propias de un usuario."""
        if user in self.users:
            return self.posts[user].view_own_posts()

    def mutual_friends(self, user1, user2):
        """Encuentra amigos mutuos entre dos usuarios."""
        if user1 in self.users and user2 in self.users:
            friends1 = self.friends[user1].in_order_traversal()
            friends2 = self.friends[user2].in_order_traversal()

            # Encuentra la intersección de los IDs de amigos
            mutual = set(friends1).intersection(set(friends2))
            return list(mutual)


# Ejemplo de uso:
social_network = Social()

# Agregar usuarios
social_network.add_user("Tito")
social_network.add_user("Teo")
social_network.add_user("Luz")
social_network.add_user("Ana")

# Establecer relaciones de amistad
social_network.add_friend("Tito", "Teo")
social_network.add_friend("Tito", "Luz")
social_network.add_friend("Teo", "Ana")
social_network.add_friend("Luz", "Ana")

# Mostrar amigos
social_network.show_friends("Tito")  # Salida: Tito's friends: ['Luz', 'Teo']

# Agregar publicaciones
social_network.add_post("Tito", "Rolen sus ID de Pokemon")
social_network.add_post("Tito", "Hola X UPY Edition")
social_network.add_post("Teo", "Guau")
social_network.add_post("Luz", "¡Qué día tan bonito!")

# Mostrar feed y publicaciones propias
print("Feed de Tito:", social_network.display_feed("Tito"))
# Salida: Feed de Tito: ['Rolen sus ID de Pokemon', 'Hola X UPY Edition']

print("Publicaciones propias de Tito:", social_network.view_own_posts("Tito"))
# Salida: Publicaciones propias de Tito: ['Hola X UPY Edition', 'Rolen sus ID de Pokemon']

# Encontrar amigos mutuos
mutual = social_network.mutual_friends("Tito", "Teo")
print("Mutual friends between Tito and Teo:", mutual)  # Salida: Mutual friends between Tito and Teo: []
