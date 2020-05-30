from common.functions import load_input


IMAGE_ROW_LEN = 25
IMAGE_COLUMN_LEN  = 6


def day8_part1():
    """
    Images are 6x25
    We need to find the layer with the least 0s
    Then on that layer count the 1s and 2s and multiply them.
    """
    data = load_input(8)[0].strip()
    data = [int(i) for i in data]
    layers = []
    least_zeros = IMAGE_ROW_LEN

    # Iterate through layers
    for i in range(0, len(data), IMAGE_ROW_LEN*IMAGE_COLUMN_LEN):
        layer = data[i:i + IMAGE_ROW_LEN*IMAGE_COLUMN_LEN]
        info = {
            "layer" : layer,
            "0s" : layer.count(0),
            "1s" : layer.count(1),
            "2s" : layer.count(2),
            "index": i,
        }
        layers.append(info)
        if info["0s"] < least_zeros:
            least_zeros = info["0s"]
            least_zeros_index = i
            result = info["1s"]*info["2s"]
    # return result, layers, least_zeros_index
    return result


def day8_part2():
    """
    Images are 6x25
    We need to find the layer with the least 0s
    Then on that layer count the 1s and 2s and multiply them.
    """
    data = load_input(8)[0].strip()
    data = [int(i) for i in data]
    picture = [2]*25*6
    # Iterate through layers building up the pic
    for i in range(0, len(data), IMAGE_ROW_LEN*IMAGE_COLUMN_LEN):
        layer = data[i:i + IMAGE_ROW_LEN*IMAGE_COLUMN_LEN]

        for index, pixel in enumerate(picture):
            if pixel != 2:
                continue
            picture[index] = layer[index]

    # Format th epic
    for i in range(0, len(picture), IMAGE_ROW_LEN):
        row = picture[i:i + IMAGE_ROW_LEN]
        print(row)

    return picture


if __name__ == "__main__":
    day8_part2()