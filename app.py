from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/pattern-result", methods=["GET", "POST"])
def pattern_result():
    try:
        return jsonify({"error": 0, "msg": "ok"})
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(debug=True, port=80)