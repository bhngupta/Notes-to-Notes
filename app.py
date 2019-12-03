# importing independent libraries
import os
from flask import Flask, render_template, request
from werkzeug import secure_filename

# importing local libraries
from ocr_core import ocr_core

app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/answer', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files["file"]
        fname = os.path.join('images/', secure_filename(f.filename))
        f.save(fname)
        answer = ocr_core(fname)
        return render_template('answer.html', answer=answer, fname=fname)


if __name__ == '__main__':
    app.run(debug=True)
