from flask import Flask, render_template
from views import views  # views.py の Blueprint をインポート
import numpy as np

app = Flask(__name__)
app.register_blueprint(views)  # Blueprint を Flask アプリに登録

if __name__ == "__main__":
    app.run(debug=True)
