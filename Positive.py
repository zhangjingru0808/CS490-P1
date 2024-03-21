import math

def count_characters_every_other_line(filename):
    total_characters = 0
    total_lines = 0

    with open(filename, 'r') as file:
        next(file)

        line_count = 0

        for line in file:

            line_count += 1

            # Check if it's an odd line
            if line_count % 2 != 0:

                num_characters = len(line.strip())
                total_characters += num_characters
                total_lines += 1

    average_length = total_characters / total_lines if total_lines != 0 else 0
    average_length = math.floor(average_length)

    return total_characters, total_lines, average_length

def create_new_file(filename, average_length):
    output_filename = filename.split('.')[0] + '_Pos_output.txt'

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
                    output_file.write(line)


def main():
    filename = input("Enter the xxxxx.txt filename: ")
    characters_count, lines_count, average_length = count_characters_every_other_line(filename)
    print(f"Total characters: {characters_count}")
    print(f"Total lines: {lines_count}")
    print(f"Average length: {average_length}")

    create_new_file(filename, average_length)
    print("Pos_output.txt File created.")

if __name__ == "__main__":
    main()

