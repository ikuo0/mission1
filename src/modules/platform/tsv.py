
def append_row(file_name: str, rows: list[list[str]]):
    with open(file_name, "w") as f:
        for row in rows:
            line_str = "\t".join(cols)
            f.write(line_str)
            f.write("\n")

def read_tsv(file_name) -> list[list[str]]:
    data = []
    with open(file_name, "r") as f:
        content = f.read()
        for row in content.split("\n"):
            data_line = []
            for col in row.split("\t"):
                data_line.append(col)
            data.append(data_line)
        return data

