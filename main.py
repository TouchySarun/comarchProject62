from all_instruction import instructions


def extracted_label(file_reader):
    label = {}
    # TODO: check same label and throw error
    for line_count, line in enumerate(file_reader):
        if not line.startswith(" "):
            current_label = line.split(maxsplit=1)[0]
            label[current_label] = line_count
    return label


def handle_instructions(line_count, line):
    # convert instuction to machine code
    split_line = line.split()
    if not line.startswith(" "):
        split_line.pop(0)  # ignore label

    instruction = split_line.pop(0).lower()
    if instruction in instructions.keys():
        fields = []
        for _ in range(instructions[instruction]):
            field = split_line.pop(0)
            # handle if field is label
            if label.get(field):
                if instruction == "beq":
                    # calculate offset
                    destination = label.get(field)
                    offset = destination - (line_count + 1)
                    field = offset
                else:
                    # field is an address of label
                    field = label.get(field)
            elif isinstance(field, float):
                raise Exception(f"{field} need to be a whole number")

            try:
                field = int(field)
            except ValueError:
                raise Exception(f"undefined label '{field}'")

            # collect field to use as input
            fields.append(field)

        return (instruction, fields)
    else:
        # error no instruction
        raise Exception("Invalid instruction")


# format label<white>instruction<white>field0<white>field1<white>field2<white>comments
if __name__ == "__main__":
    file_location = input("Input assembly file location: ")

    with open(file_location, "r") as file_reader:

        # find all lable
        label = extracted_label(file_reader)

        print(label)
        # go back to beginning of the file
        file_reader.seek(0)

        output = []

        # read each line and handle instruction
        for line_count, line in enumerate(file_reader):
            try:
                result = handle_instructions(line_count, line)
                output.append(result)
            except Exception as e:
                print(f"Error at line {line_count+1}: {e}")
                exit(1)

        for result in output:
            print(result)
