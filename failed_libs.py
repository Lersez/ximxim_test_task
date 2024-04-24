TEMPLATE_TASK_PATH = "test_task\\test_data\\test_task.pdf"
TEMPLATE_OUTPUT_FOLDER_PATH = 'test_task\output_data\\'


#VER1 - PyPDF2 3.0.1
# pip install PyPDF2
# https://pypi.org/project/PyPDF2/

## run: C:/Users/lerse/AppData/Local/Programs/Python/Python39/python.exe "D:\Work\Для собеседований\ximxim test task\test_task\ximxim_test_task\failed_libs.py"

VER = 'VER1'
import PyPDF2

def extract_text_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    text = ""

    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        text += page_obj.extract_text()

    pdf_file_obj.close()
    return text

print(extract_text_from_pdf(TEMPLATE_TASK_PATH))

# Write-Overwrites
file_out = open(TEMPLATE_OUTPUT_FOLDER_PATH + "template_" + VER + ".txt", "w")  # write mode
file_out.write(extract_text_from_pdf(TEMPLATE_TASK_PATH))
file_out.close()



#----------------------------------------------------------------------------------------------------------
#VER2 - PDFMiner
# pip install pdfminer.six
# https://pdfminersix.readthedocs.io/en/latest/

## run: C:/Users/lerse/AppData/Local/Programs/Python/Python39/python.exe "D:\Work\Для собеседований\ximxim test task\test_task\ximxim_test_task\failed_libs.py" test_task\ximxim_test_task\test_data\test_task.pdf

VER = 'VER2'
from pdfminer.high_level import extract_text

def extract_text_from_pdf(file_path):
    text = extract_text(file_path)
    return text

print(extract_text_from_pdf(TEMPLATE_TASK_PATH))

# Write-Overwrites
file_out = open(TEMPLATE_OUTPUT_FOLDER_PATH + "template_" + VER + ".txt", "w")   # write mode
file_out.write(extract_text_from_pdf(TEMPLATE_TASK_PATH))
file_out.close()




