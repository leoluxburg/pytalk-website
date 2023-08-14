from flask import Flask, render_template, send_files, redirect

app = Flask(__name__)

@app.route('/')
def ebook():
    return render_template('ebook.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/download_pdf')
def download_pdf():
    pdf_path = 'pdf/bmoebook.pdf'
    return send_file(pdf_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
