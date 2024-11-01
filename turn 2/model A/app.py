from flask import Flask, request, jsonify

app = Flask(__name__)
stakeholder_feedback = []

@app.route('/feedback', methods=['POST'])
def submit_feedback():
   data = request.get_json()
   stakeholder_feedback.append(data)
   return jsonify({"message": "Feedback submitted successfully"})

if __name__ == '__main__':
   app.run(debug=True)
