from all_instruction import instructions
from my_utils import check_allowed_label


def extracted_label(label, line, line_count):
    if not line.startswith(" "):
        line_content = line.split(maxsplit=3)
        current_label = line_content[0]

        # TODO: check new line
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

        # no error add to label
        label[current_label] = line_count

        # check .fill
        if len(line_content) >= 3:
            if line_content[1] == ".fill" and line_content[2] in label:
                label[current_label] = label[line_content[2]]


def handle_instructions(line_count, line):
    # convert instuction to machine code
    split_line = line.split()
    if not line.startswith(" "):
        split_line.pop(0)  # ignore label

    instruction = split_line.pop(0).lower()
    if instruction in instructions.keys():
        fields = []
        for _ in range(instructions[instruction]["input"]):
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
    file_output = input("File output: ")

    if file_output == "":
        file_output = "result.o"

    output = []
    with open(file_location, "r") as file_reader:

        # find all label
        label = {}
        for line_count, line in enumerate(file_reader):
            try:
                extracted_label(label, line, line_count)
            except Exception as e:
                print(f"Error at line {line_count+1}: {e}")
                exit(1)

        print(label)
        # go back to beginning of the file
        file_reader.seek(0)

        # read each line and handle instruction
        for line_count, line in enumerate(file_reader):
            try:
                result = handle_instructions(line_count, line)
                instruction_handler = instructions[result[0]]["function"]
                machine_code = instruction_handler(*result[1])
                print(machine_code)
                output.append(machine_code)
            except Exception as e:
                print(f"Error at line {line_count+1}: {e}")
                exit(1)

    # write reesult to a file
    with open(f"{file_output}", "w") as file_writer:
        for machine_code in output:
            file_writer.write(str(machine_code) + "\n")

