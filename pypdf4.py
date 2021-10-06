# extracting_text.py

from PyPDF4 import PdfFileReader


def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)

        # get the first page
        page = pdf.getPage(1)
        print(pdf.getOutlines())

        print(page)
        print('Page type: {}'.format(str(type(page))))

        text = page.extractText()
        print(text)


if __name__ == '__main__':
    path = 'report.pdf'
    text_extractor(path)
