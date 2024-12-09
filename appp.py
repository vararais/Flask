from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Mengambil data dari form
        user_input = request.form['user_input']
        # Mengirim data kembali ke halaman HTML dalam label
        return render_template('index.html', user_input=user_input)
    return render_template('index.html', user_input='')

if __name__ == '__main__':
    app.run(debug=True)