TEMPLATE_TASK_PATH = "test_data\\test_task.pdf"
TEMPLATE_OUTPUT_FOLDER_PATH = 'output_data\\'

# #----------------------------------------------------------------------------------------------------------
# #VER3 - PDFQuery
# # pip install pdfquery
# # https://pypi.org/project/pdfquery/

# ## run: C:/Users/lerse/AppData/Local/Programs/Python/Python39/python.exe "d:/Work/Для собеседований/ximxim test task/test_task/main.py" test_task\test_data\test_task.pdf
VER = 'VER3'
import pdfquery

def extract_data_from_pdf(file_path):
    pdf = pdfquery.PDFQuery(file_path)
    pdf.load()
    text = pdf.pq('LTTextLineHorizontal')

    return text

data = extract_data_from_pdf(TEMPLATE_TASK_PATH).text()
print(data)

# Write-Overwrites
file_out = open(TEMPLATE_OUTPUT_FOLDER_PATH + "template_" + VER + ".txt", "w")   # write mode
file_out.write(data)
file_out.close()
