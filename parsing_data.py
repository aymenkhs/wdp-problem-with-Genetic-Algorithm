
def parse_instance(file_path):
    content = _read_file(file_path)
    first_line, content = _separate_first_line(content)
    n, m = _first_line_content(first_line)
    # we save n and m after converting them to integers
    content = _separate_content(content)
    contents = _line_content(line)
    # we save each line maybe in a dict
    
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
    price_item = int(values[0])
    bids = values[1:]
    return price_item, bids
