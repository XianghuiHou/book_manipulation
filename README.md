# book_manipulation
Thought process

Firstly, we need to parse the text in books.json, so we import the json library then parse and print the content in books.json.
We store the json information to the variable, book_dict.

Secondly, we manually set a variable called new_book which is the new book we are going to add.
Then, we add the new book to book_dict. The new_book could be one book or multiple books.

Thirdly, we use union find and DFS to find the similar books.
We use union find to union all the similar books into one group and automatically set one of the member in that group to be the root.
All other nodes in that group will directly or indirectly point to the root of that group.
We use root_dict to store this information where the key of the root_dict is the child and the value is the parent that the child points to.
Here we use path compression to improve the time complexity of union-find algorithm.

In order to find all the members in that group efficiently, whenever we point from the child to the parent, we also need to create a revered edge which point from the parent to the child.
We use another dictionary, child_dict, to store the information so that we could use dfs later to find out all the member in that group.
