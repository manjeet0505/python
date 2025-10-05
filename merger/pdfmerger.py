from PyPDF2 import PdfWriter
merger = PdfWriter()


pdfs = []
n = int(input("Enter the number of PDF files to merge: "))
for i in range(0,n):
    pdf = input(f"Enter the path of PDF file {i+1}: ")
    pdfs.append(pdf)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_output.pdf")
merger.close()
print("PDF files merged successfully into 'merged_output.pdf'.")