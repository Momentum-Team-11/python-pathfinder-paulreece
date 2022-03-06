from pickletools import unicodestring8
from statistics import mode
from matplotlib import lines
import numpy as np
from PIL import Image as im
from PIL import ImageOps as imops
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import string


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        global array_from_file
        global percTotal
        """
        This should read all the contents of the file
        and return them as one string.
        """
        with open(self.filename) as file:
            # for line in file:
            #     # Strip out new line, turn into Tuple data-type, append to list
            #     lines.append([make_tuple(line))])
            # text_list = []
            # text_list = file.read().split("\n")
            # array_from_filey = np.loadtxt(file, dtype=str)

            array_from_file = [[int(digit) for digit in line.split()]
                               for line in file]
            array = np.array(array_from_file).astype(np.uint8)
            max = array.max()
            min = array.min()
            for num in array:
                percent = (num-min) / (max-min)
                percTotal = np.array(
                    [percent * 255]).astype(int)
                percTotal = np.full_like(array, [percTotal])
            # for i in range(len(array)):
            #     for j in range(len(array[i])):

            #         print([(array[i])])

            # totaled = np.reshape(percTotal, (-1, 600))

        return print(array, percTotal)

    def main(self):
        # array_from_file = np.reshape(1024, 720)

        # cm = plt.get_cmap('gray')
        # grayscaled = cm(array_from_file)
        # im.fromarray(np.array(grayscaled).astype(np.uint8)).save('test2.png')

        array = np.array(array_from_file).astype(np.uint8)
        # max = array.max()
        # min = array.min()
        # for num in array:
        #     percent = (num-min) / (max-min)
        # percTotal = percent * 255

        # array = array.astype(float)
        # size = 600

        # array = np.zeros((size, size, 3))
        # array[:, :, 0] = [[255]*size]*size
        # data = im.fromarray(
        #     array.astype('uint8'), 'RGB')

        data = im.fromarray(
            array, mode="L")

        image = im.open('gray.png')

        a = np.asarray(image)
        # aaa = im.fromarray(a.astype(np.uint8))
        # aaaa = np.asarray(aaa)

        data.save('test.png')
        inverted = imops.invert(data)
        inverted.save('inverted.png')
        new = im.fromarray(
            percTotal.astype(np.uint8), mode="L")
        new.save('save.png')
        inverted2 = imops.invert(new)
        inverted2.save('new.png')

        return print(array.astype(np.uint8))

    def mat(self):
        fig = plt.figure(frameon=False)
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)
        plt.imshow(np.array(array_from_file).astype(np.uint64), cmap="gray")
        print(np.array(array_from_file).astype(np.uint64))

        plt.savefig('map.png', bbox_inches='tight')
        # plt.show()

    # class WordList:
    #     def __init__(self, text):
    #         self.text = text

    #     def extract_words(self):
    #         """
    #         This should get all words from the text. This method
    #         is responsible for lowercasing all words and stripping
    #         them of punctuation.
    #         """
    #         self.text = self.text.replace("\n", "")
    #         transformed_nums = []
    #         self.list = transformed_nums
    #         for num in self.text:
    #             transformed_nums.append(num)
    #         return print(self.list)
if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = reader.read_contents()
        new_image = reader.main()
        image_show = reader.mat()

        # word_list.extract_words()
        # printer = FreqPrinter(word_list.get_freqs())
        # printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
