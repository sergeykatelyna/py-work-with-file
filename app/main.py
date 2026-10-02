import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    try:
        with open(data_file_name, "r") as input_file:
            input_lines = input_file.readlines()
    except FileNotFoundError:
        print("Give me the file!")
        return

    input_data = {}
    for input_line in input_lines:
        if not input_line.strip():
            continue
        name, value = input_line.strip().split(",")
        input_data[name] = input_data.get(name, 0) + int(value)

    if not input_data:
        print("Your file is empty!")
        return

    input_data_report = {
        "supply": input_data["supply"],
        "buy": input_data["buy"],
        "result": input_data["supply"] - input_data["buy"]
    }

    with open(
        report_file_name,
        "w",
        newline="",
        encoding="utf-8"
    ) as output_file:
        writer = csv.writer(output_file)
        writer.writerows(input_data_report.items())
