import os
from os import path
from fpdf import FPDF
from PIL import Image


PIC_EXTS = ['.jpg', '.png']


def make_comics(folder: str):
    print('start process {0}\n'.format(folder))
    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_auto_page_break(0)
    pdf.set_margins(0, 0, 0)

    images = []
    for file in os.listdir(folder):
        if path.splitext(file)[1].lower() in PIC_EXTS:
            images.append(path.join(folder, path.join(folder, file)))
    images.sort()

    for image in images:
        pdf.add_page()

        img = Image.open(image)
        w, h = img.size
        img.close()

        if (h / w) > (pdf.h / pdf.w):
            w_mm = pdf.h * (w / h)
            x = (pdf.w - w_mm) / 2
            pdf.image(image, x=x, h=pdf.h)
        else:
            h_mm = pdf.w * (h / w)
            y = (pdf.h - h_mm) / 2
            pdf.image(image, y=y, w=pdf.w)

    file_name = '{parent}/{name}.pdf'.format(parent=path.dirname(folder), name=path.basename(folder))
    pdf.output(file_name)
    print('finished {0}\n'.format(file_name))
