class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''
    #Initialized the EmployeeNode class with the attributes name, left, and right
    #Stored the employee's name in self.name variable and initialized left and right positions as None
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
#Tested that the attributes initialized correctly
employee_1 = EmployeeNode("John")
print(employee_1.name)
print(employee_1.left)
print(employee_1.right)

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    #Initialized TeamTree class with an empty root
    def __init__(self):
        self.root = None
    #Defined a method to insert values into the team tree
    def insert(self, manager_name, employee_name, side, current_node=None):
        #Check if a team lead has already been added to the tree and print error message if not
        if self.root is None:
            print("Error: Please add a team lead first.")
            return 
        #Determine if this is the original call to insert()
        starting_call = current_node is None
        #Begin search at the root if no node is provided
        if current_node is None:
            current_node = self.root
        #Check whether the current employee is the specified manager
        if current_node.name == manager_name:
            #Handle request to add an employee to the left side
            if side == "left":
                if current_node.left is None:
                    #Create a new node and set it as the left child and print success message
                    current_node.left = EmployeeNode(employee_name)
                    print(f"{employee_name} added to the left of {manager_name}.")
                else:
                    #If left side is taken, print error message
                    print(f"Error: The left side of {manager_name} is taken.")
            #Handle request to add an employee to the right side
            elif side == "right":
                if current_node.right is None:
                    #Create a new node and set it as the right child and print success message
                    current_node.right = EmployeeNode(employee_name)
                    print(f"{employee_name} added to the right of {manager_name}.")
                else:
                    #If right side is taken, print error message
                    print(f"Error: The right side of {manager_name} is taken.")
            
            else:
                #Print error message for values other than left and right
                print("Error: Please enter left or right.")
            #Stops searching if the manager was found
            return True
        
        #Search the left subtree for the specified manager
        if current_node.left is not None:
           found = self.insert(manager_name, employee_name, side, current_node.left)
           #Stop searching if the manager was found
           if found:
               return True
        #Search the right subtree for the specified manager
        if current_node.right is not None:
           found = self.insert(manager_name, employee_name, side, current_node.right)
           #Stop searching if the manager was found, even if insertion fails
           if found:
               return True
        #Print an error message if the manager was not found in the original call
        if starting_call:
            print(f"Error: Manager '{manager_name}' was not found.")
        #Return false if the manager was not found in this subtree
        return False
    #Define a method to print the team tree
    def print_tree(self, node=None, level=0):
        #Start at the root when print_tree() is called without a node
        if node is None:
            if level == 0:
                node = self.root
            else:
                #Stops when a recursive call reaches an empty child
                return
        #Print a message when the tree is empty
        if node is None:
            print("The team tree is empty.")
            return
        #Print the employee with indentation based on their level in the hierarchy
        print("  " * level + "- " + node.name)
        #Recursively print the left and right subtrees
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)

# Test your code here
test_tree = TeamTree()
test_tree.root = EmployeeNode("Ms. Manager") 
test_tree.insert("Ms. Manager", "Employee #1", "right")
test_tree.insert("Ms. Manager", "Employee #2", "left")
print(test_tree.root.right.name) # Employee #1
print(test_tree.root.left.name) # Employee #2

test_tree.root = EmployeeNode("Jordan")
test_tree.insert("Jordan", "Taylor", "right")
test_tree.insert("Jordan", "Riley", "left")
test_tree.insert("Riley", "Dana", "right")
test_tree.insert("Riley", "Morgan", "left")
#Tested program behavior when the manager can't be found
test_tree.insert("Manager", "Employee", "left")
test_tree.print_tree()
#Tested program behavior with an empty tree
empty_tree = TeamTree()
empty_tree.print_tree()
empty_tree.insert("Jordan", "Taylor", "left")
#Tested program behavior when adding an employee under a manager several levels down
deep_tree = TeamTree()
deep_tree.root = EmployeeNode("Jordan")
deep_tree.insert("Jordan", "Riley", "left")
deep_tree.insert("Riley", "Morgan", "left")
deep_tree.insert("Morgan", "Cassidy", "right")
deep_tree.print_tree()
#Tested program behavior when adding an employee to an occupied left and right side and with an invalid side
deep_tree.insert("Jordan", "Alex", "left")
deep_tree.insert("Morgan", "Sam", "right")
deep_tree.insert("Jordan", "Alex", "middle")

# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

#Called the company_directory function to run the program
company_directory()

#Write Your Design Memo
#At the bottom of your file or in a separate .txt file, include a short reflection (200–300 words)
# that answers the following questions:

# How did recursive insertion work?
# What challenges did you face when finding the right spot for a new employee?
# When might trees be preferable to other data structures in real-world systems?

#The company directory works by utilizing a binary tree to store employee names in individual 
#nodes that represent relationships within a company hierarchy. This program includes an 
#EmployeeNode class to store each employee's name and references to their left and right child 
#nodes, as well as a TeamTree class to manage the tree and store a root that holds the team lead. 
#The insert() and print_tree() methods use recursion to search through the tree, add new employees,
# and display the company hierarchy. For example, in the insert() method, the current node is 
#checked to determine if its name matches the manager who the new employee should report to. 
#If the manager is not found at that node, the method recursively searches the left and right 
#subtrees until it finds the appropriate manager or determines that the manager does not exist. 
#Once the manager is found, the method checks whether the requested position is available before 
#adding the new employee. One challenge I faced was handling situations in which a manager could 
#not be found, or a position was already occupied, while also making sure that recursive calls 
#stopped searching once the manager was located. Trees are preferable to other data structures 
#when managing hierarchical information, such as employee reporting relationships or folders 
#within a computer's file system. Compared with a flat list, a tree makes parent-child 
#relationships easier to represent and navigate, although a binary tree may not be appropriate 
#for a company where managers supervise more than two employees.