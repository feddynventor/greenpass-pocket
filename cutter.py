import time
import fitz

from server import UPLOAD_FOLDER

def pocketize(file_dir):
    doc = fitz.open(file_dir)
    page = doc.load_page(0)

    # pix = page.get_pixmap()  #full page

    mat = fitz.Matrix(2, 2)  # zoom factor 2 in each direction
    rect = page.rect  # the page rectangle

    clip = fitz.Rect(rect.bl/2, fitz.Point(rect.width/2, rect.height))

    pix = page.get_pixmap(matrix=mat, clip=clip)

    result_filename = str(int(time.time()))+'.png'
    pix.save(UPLOAD_FOLDER+result_filename)
    return result_filename
