import string

def designerPdfViewer(h, word):
    h = dict(zip(string.ascii_lowercase, h))
    heights = [int(h[char]) for char in word]
    return max(heights) * len(word)

if __name__ == '__main__':

    print(designerPdfViewer('1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5', 'abc'))
    print(designerPdfViewer('1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7', 'zaba'))