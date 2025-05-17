
def write_and_append_to_file(filename):
   
    user_input = input("Enter data to write to the file: ")
    with open(filename, "w") as file:
        file.write(user_input + "\n")

   
    additional_input = input("Enter additional data to append to the file: ")
    with open(filename, "a") as file:
        file.write(additional_input + "\n")

   
    print("\nFinal content of the file:")
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())

write_and_append_to_file("output.txt")