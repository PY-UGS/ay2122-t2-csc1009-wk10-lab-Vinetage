# Modules dictionary for name reference
ModuleContainer = {
    "CSC1006":"Mathematics 2",
    "CSC1007":"Operating Systems",
    "CSC1008":"Data Structures and Algorithms",
    "CSC1009":"Object-Oriented Programming",
    "CSC1010":"Computer Networks"
}
# Function to get module name using module code
def ModuleName(moduleCode):
    # Check if module code is in dictionary
    if ModuleContainer.get(moduleCode) is not None:
        # Return the value
        return ModuleContainer[moduleCode]
    # Class does not exist
    return "Invalid Class"
# Main
if __name__ == '__main__':
    # Question 2B
    print("Week 01 Q2B")
    # Print a prompt for user
    moduleCode = input("Input module code: ")
    # Print module name
    print(ModuleName(str.upper(moduleCode)))
    # Question 2C
    print("Week 01 Q2C")
    # For loop from 102 to 66 and print odd numbers only
    for x in range (102,66,-1):
        if x % 2 != 0:
            print(x)
