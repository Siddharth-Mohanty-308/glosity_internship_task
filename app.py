from flask import Flask,render_template,request
from text_summarizer import summarizer

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['GET', 'POST'])
def summarize_page():
    if request.method == 'POST':
        input_text = request.form['text']
        summary, text, length_of_text, length_of_summary = summarizer(input_text,int(len(input_text.split("."))*0.3))
        return render_template('analyze.html', summary=summary, original_text=text, len_of_text=length_of_text,len_of_summary=length_of_summary)

if __name__ == '__main__':
    app.run(debug=True)    