from application import app
from application import data_access;

app.config['SECRET_KEY'] = "YIPPE"
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)



