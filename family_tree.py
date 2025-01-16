class Person:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def print_family_tree(person, level=0):
    print(' ' * level * 4 + person.name)
    for child in person.children:
        print_family_tree(child, level + 1)

# Example usage
grandparent = Person("Grandparent")
parent1 = Person("Parent1", grandparent)
parent2 = Person("Parent2", grandparent)
grandparent.add_child(parent1)
grandparent.add_child(parent2)

child1 = Person("Child1", parent1)
child2 = Person("Child2", parent1)
parent1.add_child(child1)
parent1.add_child(child2)

child3 = Person("Child3", parent2)
parent2.add_child(child3)

print("Family Tree:")
print_family_tree(grandparent)
