from flask import Flask,request,render_template
from PyPDF2 import PdfReader
import re
app = Flask(__name__)
def verify_text(text):
    credit=re.search("\d{4}-\d{4}-\d{4}",text)
    phone_number=re.search("\d{2}\s\d{3}\s\d{3}",text)
    email=re.search("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Z,a-z]{2,3}", text)
    date = re.search("(\d{2}-\d{1,2}-\d{4})",text)
    
    if date :
     date1=re.findall("(\d{2}-\d{1,2}-\d{4})",text)
   
    if email :
     email1=re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Z,a-z]{2,3}",text)
   
    if credit:
     credit_card1=re.findall("\d{4}-\d{4}-\d{4}",text)
     
    if phone_number:
     phn1=re.findall("\d{2}\s\d{3}\s\d{3}",text)
    return ("date of creation:",date1,"phone number:",phn1,"Email:",email1,"credit card:",credit_card1)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']

        
        pdf_reader = PdfReader(pdf_file)
        text = ''
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text()
        result =verify_text(text)
        
        return render_template('main.html', result=result)

    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
