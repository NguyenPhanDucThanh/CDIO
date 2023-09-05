from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('homepage.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' in request.files:
        image = request.files['image']
        image.save(os.path.join('static', 'uploads', image.filename))
        return redirect(url_for('show_image', filename=image.filename))

@app.route('/show/<filename>')
def show_image(filename):
    uploaded_image_url = url_for('static', filename='uploads/' + filename)
    return render_template('result.html', uploaded_image_url=uploaded_image_url)



if __name__ == '__main__':
    app.run(debug=True)
