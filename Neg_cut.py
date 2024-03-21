def create_new_file(filename, average_length):
    output_filename = filename.split('.')[0] + '_output.txt'

    with open(filename, 'r') as file, open(output_filename, 'w') as output_file:
        line_count = 0

        for line in file:

            line_count += 1

            # If it's an odd line, pair it with the next line
            if line_count % 2 != 0:
                next_line = next(file, None) 
                if next_line is not None:
                    
                    if len(next_line.strip()) > average_length:
                        
                        output_file.write(line)
                        output_file.write(next_line[:int(average_length)] + '\n')

                    else:
                        #skip both lines
                        continue
                else:
                    # If there is no next line, just write the odd line
                    output_file.write(line[:int(average_length)] + '\n')
                



def main():
    filename = input("Enter the xxxxxxx_Neg.bed filename: ")
    average_length = input("Enter the average length: ")
    average_length = int(average_length)

    create_new_file(filename, average_length)
    print("Neg_output.txt File created.")

if __name__ == "__main__":
    main()