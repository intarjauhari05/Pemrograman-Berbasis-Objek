class Item():
    def __init__(self, Code=0, Title='', Description='', Category='', Picture='', QuantityInStock=0, Price=0):
        self.Code = Code
        self.Title = Title
        self.Description = Description
        self.Category = Category
        self.Picture = Picture
        self.QuantityInStock = QuantityInStock
        self.Price = Price

    def viewFullDescription(self):
        pass 

    def addToCart(self):
        pass

    def updateStockLevel(self):
        pass

class DVD(Item):
    def __init__(self, Director='', Certificate='', ListofActor='', Code=0, Title='', Description='', Category='', Picture='', QuantityInStock=0, Price=0):
        super().__init__(Code, Title, Description, Category, Picture, QuantityInStock, Price)
        self.Director = Director
        self.Certificate = Certificate
        self.ListofActor = ListofActor

class MP3(Item):
    def __init__(self, Duration=0, Artist='', Code=0, Title='', Description='', Category='', Picture='', QuantityInStock=0, Price=0):
        super().__init__(Code, Title, Description, Category, Picture, QuantityInStock, Price)
        self.Duration = Duration
        self.Artist = Artist

    def playExtract(self):
        pass

    def download(self):
        pass

class Book(Item):
    def __init__(self, ISBN=0, Author='', Synopsis='', Code=0, Title='', Description='', Category='', Picture='', QuantityInStock=0, Price=0):
        super().__init__(Code, Title, Description, Category, Picture, QuantityInStock, Price)
        self.ISBN = ISBN
        self.Author = Author
        self.Synopsis = Synopsis

    def preview(self):
        pass

dvd1 = DVD(
    201,
    "Inception",
    "Film thriller fiksi ilmiah",
    "Film",
    "inception.jpg",
    15,
    75000,
    "Christopher Nolan",
    "PG-13",
    "Leonardo DiCaprio, Joseph Gordon-Levitt"
)

mp3_1 = MP3(
    301,
    "Bohemian Rhapsody",
    "Audio trek original",
    "Audio",
    "bohemian.jpg",
    50,
    15000,
    354, 
    "Queen"
)

buku1 = Book(
    401,
    "Laskar Pelangi",
    "Novel fiksi Indonesia",
    "Buku",
    "laskar.png",
    25,
    85000,
    978602291,
    "Andrea Hirata",
    "Kisah sepuluh anak di Belitung."
)