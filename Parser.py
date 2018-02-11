
#
def spliter(string):
    counter = 0

    line = string.split(";") # Split the initial line

    # Print the rest of the line
    for split in line:
        if ',' in split:
            commasplit = split.split(",")
            for commavalue in commasplit:
                counter += 1

                output_file.write("\tComma Split " + str(counter) + ": " + commavalue.strip('\n') + ",\n")
                # print("\tSplit " + str(counter) + ": " + commavalue + ",\n")
        else:
            counter+=1
            output_file.write("\tSemi Colon Split " + str(counter) + ": " + split.strip('\n') + ";\n")
            # print("\tSplit " + str(counter) + ": " + split + ";\n")



try:
    input_file_name = input("What is the EWS log named?\n")  # Gets the name of the EWS log we are parsing
    # input_file_name = ""

    output_file_name = input("What is the name of the output file? Use underscores instead of spaces\n")

    input_file = open(input_file_name, "r")
    output_file = open(output_file_name, "w")
    # output_file = open("", "w")
    entry = 0
    for line in input_file:
        entry+=1
        output_file.write("\nEntry " + str(entry) + ": \n")
        spliter(line)


except IOError:
     print("File could not be open.")
except KeyboardInterrupt:
    print("You have cancelled the operation")

    output_file.close()
    input_file.close()