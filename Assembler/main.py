from all_instruction import instructions
from my_utils import check_allowed_label


def extracted_label(label, line, line_count, line_content):

    current_label = line_content[0]

    illegal_character = check_allowed_label(current_label)
    # check error
    if illegal_character:
        raise Exception(f"Label {current_label} can't contain {illegal_character}")
    elif current_label[0].isdigit():
        raise Exception(f"Label {current_label} can't start with number")
    elif len(current_label) > 6:
        raise Exception(f"Label {current_label} can't be more than 6 character")
    elif label.get(current_label):
        raise Exception(f"Duplicate label {current_label}")

    label[current_label] = line_count


def handle_instructions(line_count, line_content, label):

    instruction = line_content.pop(0).lower()
    if instruction in instructions.keys():
        fields = []
        for _ in range(instructions[instruction]["input"]):

            # handle not enough field for instruction
            try:
                field = line_content.pop(0)
            except IndexError:
                raise Exception(f"Not enough field for {instruction}")

            # handle if field is label
            label_value = label.get(field)
            if label_value:
                if instruction == "beq":
                    # calculate offset
                    destination = label_value
                    offset = label_value - (line_count + 1)
                    field = offset
                else:
                    # field is an address of label
                    field = label_value

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
    file_output = input("File output: ")

    if file_output == "":
        file_output = "result.o"

    output = []
    with open(file_location, "r") as file_reader:

        # find all label
        label = {}
        address_line = 0
        for line_count, line in enumerate(file_reader):
            try:
                line_content = line.split(maxsplit=3)[:3]
                # ignore blank line
                if len(line_content) > 0:

                    if not line.startswith(" "):
                        extracted_label(label, line, address_line, line_content)
                    address_line += 1

            except Exception as e:
                print(f"Error at line {line_count+1}: {e}")
                exit(1)

        print(label)
        # go back to beginning of the file
        file_reader.seek(0)

        # read each line and handle instruction
        address_line = 0
        for line_count, line in enumerate(file_reader):
            try:
                # convert instuction to machine code
                line_content = line.split()
                if len(line_content) > 0:

                    if line_content[0] not in instructions.keys():
                        line_content.pop(0)  # ignore label

                    instruction, fields = handle_instructions(
                        address_line, line_content, label
                    )
                    instruction_handler = instructions[instruction]["function"]
                    machine_code = instruction_handler(*fields)
                    print(machine_code)
                    output.append(machine_code)
                    address_line += 1

            except Exception as e:
                print(f"Error at line {line_count+1}: {e}")
                exit(1)

    # write reesult to a file
    with open(f"{file_output}", "w") as file_writer:
        for machine_code in output:
            file_writer.write(str(machine_code) + "\n")

