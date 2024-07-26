from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# URL of your main application
MAIN_APP_URL = 'https://tw8doum2ob.execute-api.ap-south-1.amazonaws.com/anivault'

@app.route('/', methods=['GET', 'POST'])
def delete_user_form():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Send delete request to main application
        response = requests.post(f'{MAIN_APP_URL}/user/delete', data={'email': email, 'password': password})
        
        return jsonify({
            'status': 'success' if response.status_code == 200 else 'error',
            'message': response.json().get('message', 'Unknown error')
        })
    
    return render_template('delete_form.html')

if __name__ == '__main__':
    app.run(debug=True)