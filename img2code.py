import cv2
import sys
import math


def convert(scale: int) -> str:
    pixels = [' ', ':', 'O', 'M']
    return pixels[math.floor(scale * len(pixels) / 256)]


def imgToCode(img: str) -> str:
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    out = "\n".join(
        map(lambda x: ''.join(x), map(lambda xs: map(convert, xs), img)))
    return out


def saveCode(img: str, ext: str = "txt", name: str = "output"):
    file = open((name+"."+ext), "w+")
    if ext == "py":
        out = "\"\"\"\n" + img + "\n\"\"\"\n"
    elif ext in ["c", "cpp", "cs", "js", "ts", "java", "swift"]:
        out = "/*\n" + img + "\n*/\n"
    elif ext == "hs":
        out = "{-\n" + img + "\n-}\n"
    else:
        out = img
    file.write(out)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        raise Exception("Expect at least 1 argument.")
    elif len(args) == 2:
        saveCode(imgToCode(args[1]))
    elif len(args) == 3:
        saveCode(imgToCode(args[1]), "txt", args[2])
    else:
        saveCode(imgToCode(args[1]), args[3], args[2])
