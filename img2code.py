import cv2
import sys


def convert(pix):
    if 0 <= pix < 63:
        return ' '
    elif 64 <= pix < 127:
        return ':'
    elif 128 <= pix < 191:
        return 'O'
    else:
        return 'M'


def imgToCode(img: str) -> str:
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    y = "\n".join(
        list(map(lambda x: ''.join(x), map(lambda xs: map(convert, xs), img))))
    return y


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
    a = sys.argv
    if len(a) < 2:
        raise "Expect at least 1 argument."
    elif len(a) == 2:
        saveCode(imgToCode(a[1]))
    elif len(a) == 3:
        saveCode(imgToCode(a[1]), "txt", a[2])
    else:
        saveCode(imgToCode(a[1]), a[3], a[2])
