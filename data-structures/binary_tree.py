class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data <= self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def contains(self, data):
        return (self.data == data or
                (self.left and self.left(contains(data))) or
                (self.right and self.right(contains(data))))

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print(self.data)
        if self.right:
            self.right.print_in_order()

    def print_pre_order(self):
        print(self.data)
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()

    def print_post_order(self):
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()
        print(self.data)

    def __repr__(self):
        """a bad repr, but useful for quick poking in repl"""
        if self.left and self.right:
            fmt = "   {}\n" + \
                  "  /  \\\n" + \
                  "{}    {}"
            return fmt.format(self.data, self.left.data, self.right.data)
        elif self.left:
            fmt = "   {}\n" + \
                  "  /  \\\n" + \
                  "{}"
            return fmt.format(self.data, self.left.data)
        elif self.right:
            fmt = "   {}\n" + \
                  "  /  \\\n" + \
                  "      {}"
            return fmt.format(self.data, self.right.data)
        fmt = "   {}\n" + \
              "  /  \\"
        return fmt.format(self.data)


