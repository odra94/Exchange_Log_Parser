

def splitter(string):
    counter = 0

    line = string.split(";") # Split the initial line

    # Print the rest of the line
    for split in line:
        if ',' in split:
            commasplit = split.split(",")
            for commavalue in commasplit:
                counter += 1

                output_file.write("\tSplit " + str(counter) + ": " + commavalue.strip('\n') + ",\n")
                # print("\tSplit " + str(counter) + ": " + commavalue + ",\n") #Used for debugging
        else:
            counter+=1
            output_file.write("\tSplit " + str(counter) + ": " + split.strip('\n') + ";\n")
            # print("\tSplit " + str(counter) + ": " + split + ";\n") # Used for debugging


print("To exit program once it is running press \"Ctrl+C\" on your keyboard or close the program.")
while True:
    # print("To exit program once it is running press \"Ctrl+C\" on your keyboard or close the program.")
    try:
        input_file_name = input("What is the name of log you are trying to parse? Include extension.\n")  # Gets the name of the EWS log we are parsing
        # input_file_name = "test_file.txt" Used for debugging

        output_file_name = input("Name parsed output file corresponding to file: "+ input_file_name +". Include extension.\n")

        input_file = open(input_file_name, "r") # open input log file to parse
        output_file = open(output_file_name, "w") # open output result file to write to
        # output_file = open("output.txt", "w") # Used for debugging

        entry = 0
        for line in input_file:
            entry+=1
            output_file.write("\nEntry " + str(entry) + ": \n")
            splitter(line)


    except IOError:
         print("File could not be open.")
    except KeyboardInterrupt:
        print("You have cancelled the operation")

        # Closing files before exiting program
        output_file.close()
        input_file.close()