from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    array_name = data.get("arrayName", "array_name")
    raw_text = data.get("rawData", "")
    
    # Parse the table into float arrays
    rows = raw_text.strip().splitlines()
    output = []
    for row in rows:
        numbers = [float(val.replace(',', '.')) for val in re.findall(r"[\d,]+", row)]
        output.append(numbers)
    
    # Format as NumPy-like array
    result = f"{array_name} = [\n"
    for row in output:
        result += "    " + str(row) + ",\n"
    result += "]"

    return jsonify({"converted": result})

if __name__ == "__main__":
    app.run(debug=True)
