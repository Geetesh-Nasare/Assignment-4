def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
    print("Data successfully written to", filename)

def append_to_file(filename, additional_data):
    with open(filename, 'a') as file:
        file.write(additional_data)
    print("Data successfully appended.")

def read_file_content(filename):
    with open(filename, 'r') as file:
        return file.read()

def main():
    filename = 'output.txt'
    
    user_input = input("Enter text to write to the file: ")
    write_to_file(filename, user_input + '\n')
    
    additional_input = input("Enter additional text to append: ")
    append_to_file(filename, additional_input + '\n')
    
    final_content = read_file_content(filename)
    print("\nFinal content of", filename + ":")
    print(final_content)

if __name__ == "__main__":
    main()
