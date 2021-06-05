
from instance import Bid, InstanceWDP

def parse_instance(file_path):
    content = _read_file(file_path)

    first_line, content = _separate_first_line(content)
    n, m = _first_line_content(first_line)

    content = _separate_content(content)

    bids = []
    for line in content:
        price, items = _line_content(line)
        bids.append(Bid(content.index(line), price, items))

    return InstanceWDP(n, m, bids)

def _read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

def _separate_first_line(content):
    # find the index of the first '\n'
    index = content.find('\n')
    first_line = content[:index]
    content = content[index+1:]
    return first_line, content

def _separate_content(content):
    lines = content.split("\n")
    return lines[:-1] # we remove the last line which is ''

def _first_line_content(first_line):
    values = first_line.split(' ')
    n = int(values[0])
    m = int(values[1])
    return n, m

def _line_content(line):
    values = line.split(' ')
    price = float(values[0])
    items = values[1:]
    items = [int(item) for item in items]
    return price, items
