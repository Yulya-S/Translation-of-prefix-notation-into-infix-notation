def translate_to_infix(line: str):
    line = line.split(' ')
    operations = []
    numbers = []
    for i in line:
        if i in '+-*/':
            operations.append(i)
        else:
            try:
                float(i)
                numbers.append(i)
            except:
                return None
    line = ''
    while (len(operations) > 0 and len(numbers) > 0):
        line += f"{numbers.pop(0)} "
        line += f"{operations.pop(0)} "
    if line[-2] in '+-*/':
        if len(numbers) == 0:
            line = line[:-3]
        else:
            line += numbers[0]
    if len(line) <= 2:
        return ''
    return line
