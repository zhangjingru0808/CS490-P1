def create_new_file(filename):
    output_filename = filename.split('.')[0] + '_Neg.txt'

    with open(filename, 'r') as file, open(output_filename, 'w') as output_file:

        for line in file:

            first_char = line.split('\t')[0]
            start_string = line.split('\t')[2]
            next_line = next(file, None)
            start_number = int(start_string) + 1

            if next_line is not None:
                end_string = next_line.split('\t')[1]
                end_number = int(end_string) - 1

                if end_number <= start_number:
                    continue

                output_file.write(first_char + '\t' + str(start_number) + '\t' + str(end_number) + '\n')



def main():
    filename = input("Enter the xxxxx.bed filename: ")
    create_new_file(filename)
    print("Neg.txt File created.")

if __name__ == "__main__":
    main()