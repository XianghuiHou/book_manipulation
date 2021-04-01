import json

class Book:
    def __init__(self):
        self.book_dict = {}
        self.root_dict = {} # Store the root of each node(book) in order to use union_find algorithm
        self.child_dict = {} # Store the reversed edge of root_dict in order to use dfs when finding similar books


    # read all the books from the "books.json" and print them in pretty format
    def read_book(self):
        with open("books.json") as f:
            self.book_dict = json.load(f)
            self.union(self.book_dict)
        print(json.dumps(self.book_dict, indent = 4))


    # add one book(or multiple books) to the "books.json"
    def add_book(self, new_book):
        for key in new_book.keys():
            self.book_dict[key] = new_book[key]
        self.union(new_book)
    
        with open('books.json', 'w') as f:
            json.dump(self.book_dict, f, indent=4)


    # find all the similar books to the one passed into this function
    def find_similar_books(self, book):
        member_set = set()
        self.dfs(self.find_root(book), member_set)
        member_set.remove(book)
        print(list(member_set))


    # use dfs to find all the similar books by traversing the graph in child_dict
    # use member_set (hash set) to store the node that we have visited so we could avoid repeatedly visiting the same nodes
    def dfs(self, node, member_set):
        if node in member_set:
            return
        member_set.add(node)
        if node not in self.child_dict:
            return
        for next_node in self.child_dict[node]:
            self.dfs(next_node, member_set)


    # use union-find to store the root of each group
    def union(self, new_dict):
        for k, v in new_dict.items():
            for sb in v['similar_books']:
                r1 = self.find_root(sb)
                r2 = self.find_root(k)
                self.root_dict[r1] = r2
                if r2 not in self.child_dict:
                    self.child_dict[r2] = set()
                self.child_dict[r2].add(r1)


    # we have stored the temporarily direct root of each node in root_dict
    # find the root of the group that the node stays in
    # path compression: set the root of the node to be the root of the group in order to make the searching root process quickly next time
    def find_root(self, book):
        if book not in self.root_dict or self.root_dict[book] == book:
            return book
        new_root = self.find_root(self.root_dict[book])
        if self.root_dict[book] != new_root:
            self.child_dict[self.root_dict[book]].remove(book)
            self.root_dict[book] = new_root
            self.child_dict[new_root].add(book)

        return self.root_dict[book]


book_object = Book()
book_object.read_book()

new_book = {"b0007": {
                "book_id": "b0007",
                "title": "title7",
                "author": "author name",
                "category": "category name",
                "similar_books": [
                    "b005",
                    "b009",
                    "b001"
                ]
            },
            "b0008": {
                "book_id": "b0008",
                "title": "title8",
                "author": "author name",
                "category": "category name",
                "similar_books": [
                    "b005",
                    "b009",
                    "b001"
                ]
            }}

book_object.add_book(new_book)
book_object.find_similar_books("b0001")
book_object.find_similar_books("b0002")
book_object.find_similar_books("b0003")
book_object.find_similar_books("b0004")
book_object.find_similar_books("b0005")
book_object.find_similar_books("b0006")
