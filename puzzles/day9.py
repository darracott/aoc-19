from common.functions import load_input
from common.classes import IntCodeComputer


def day9_part1():
    """
    Run test intcode.
    """
    data = load_input(9)[0].strip()
    intcode = [int(x) for x in data.split(",")]
    boost_computer = IntCodeComputer(intcode=intcode)
    # Run in Test mode by providing input 1.
    boost_computer.queue_input(1)
    boost_computer.run()
    print(boost_computer.outputs)





# def day8_part2():
#     """
#     Images are 6x25
#     We need to find the layer with the least 0s
#     Then on that layer count the 1s and 2s and multiply them.
#     """
#     data = load_input(8)[0].strip()
#     data = [int(i) for i in data]
#     picture = [2]*25*6
#     # Iterate through layers building up the pic
#     for i in range(0, len(data), IMAGE_ROW_LEN*IMAGE_COLUMN_LEN):
#         layer = data[i:i + IMAGE_ROW_LEN*IMAGE_COLUMN_LEN]

#         for index, pixel in enumerate(picture):
#             if pixel != 2:
#                 continue
#             picture[index] = layer[index]

#     # Format th epic
#     for i in range(0, len(picture), IMAGE_ROW_LEN):
#         row = picture[i:i + IMAGE_ROW_LEN]
#         print(row)

    # return picture


if __name__ == "__main__":
    day9_part1()