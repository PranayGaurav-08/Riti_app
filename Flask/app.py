from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Global list to store submitted numbers
stored_values = []

# HTML template with input box and submit button
html_form = '''
<!doctype html>
<title>Home</title>
<h2>Enter a number:</h2>
<form method="POST" action="/data">
  <input type="number" name="number" required>
  <input type="submit" value="Submit">
</form>
'''

@app.route('/home', methods=['GET'])
def home():
    return render_template_string(html_form)

@app.route('/data', methods=['GET', 'POST'])
def data():
    global stored_values

    if request.method == 'POST':
        # Get number from form submission
        number = request.form.get('number') or request.json.get('number')

        try:
            number = int(number)
            stored_values.append(number)
            return f"Number {number} added successfully!"
        except (TypeError, ValueError):
            return "Invalid input. Please enter a valid integer.", 400

    elif request.method == 'GET':
        # Return list as { "key": [list] }
        return jsonify({"values": stored_values})

# Optional endpoint to clear data (for testing)
@app.route('/clear', methods=['POST'])
def clear_data():
    stored_values.clear()
    return "List cleared!"

if __name__ == '__main__':
    app.run(debug=True)
