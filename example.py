def file_opration():

    try:

        filename = input("enter the name of the file you want to read from, eg (file1.txt): ")

        with open(filename,"r") as input_file:
            contents = input_file.read()


            word_count = len(contents.split())
            uppercase_contents = contents.upper()

        with open('modified_'+filename,'w') as output_file:
            output_file.write("modified text (uppercase): \n")
            output_file.write(uppercase_contents + "\n\n")
            output_file.write(f"word_count: {word_count}")

        print(f"successful process.. written to 'modified_{filename}'.")

    except FileNotFoundError:
        print("error: file not found.. check the filename and try again")
    except PermissionError:
        print('error: you do not have permission to write on this file')
    except Exception as e:
        print(f'an unexpected error occured : {e}')

file_opration()
