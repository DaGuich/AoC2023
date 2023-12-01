# just used to read the input file
from pathlib import Path

# digits as chars
from string import digits


def process(lines: list[str]) -> int:
    # remove whitespace
    lines = map(lambda line: line.strip(), lines)
    # filter for empty lines
    lines = filter(lambda line: len(line) > 0, lines)
    # filter for digits in lines
    lines = map(lambda line: filter(lambda c: c in digits, line), lines)
    # join digits (char) to one string per line
    nums = map(lambda line: ''.join(line), lines)
    # create int out of first digit and last digit
    nums = list(map(lambda num: int(num[0] + num[-1]), nums))
    # return sum
    return sum(nums)


if __name__ == '__main__':
    input_file = Path(__file__).parent / 'input.txt'

    # first test with test input
    example = """
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """
    assert process(example.split('\n')) == 142

    # process actual data
    with input_file.open() as f:
        result = process(f.readlines())
        print(result)


