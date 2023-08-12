from flask import Flask, render_template, send_file, redirect
import requests
import json

app = Flask(__name__)

@app.route('/')
def ebook():
    return render_template('ebook.html')

@app.route('/pago')
def pago():
  data = {
    "CCLW": "A5D93FECC07735355E7C8D640F88922E29068A9CB02423EFF8E2FB48170EFB8A4B779B38E81DF567990CEDDC4999AA4DDB57D3AFDAF4C7B5C1BB1545A99BD0AB", #Llave de usuario,
    "CMTN": 1.99, #Precio,
    "CDSC": "BMOEBOOK", #Descripción,
    "RETURN_URL": "https://www.leonardoluxburg.com/thank_you"
  }

  url = 'https://sandbox.paguelofacil.com/LinkDeamon.cfm'

  response = requests.post(url, data=data)
  result = response.text

  data = json.loads(result)
  code = data['headerStatus']['code']

  if code != 200:
    return print('erro')
  else:
    return redirect(data['data']['url'])

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/download_pdf')
def download_pdf():
    pdf_path = 'pdf/bmoebook.pdf'
    return send_file(pdf_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
