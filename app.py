from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# HTML content directly in the app
index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Form</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        form {
            background: #ffffff;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            width: 100%;
        }
        h2 {
            text-align: center;
            color: #333;
            margin-bottom: 20px;
            font-size: 24px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #555;
        }
        input, select {
            width: 100%;
            padding: 12px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
            transition: border-color 0.3s ease;
        }
        input:focus, select:focus {
            border-color: #007BFF;
            outline: none;
        }
        button {
            width: 100%;
            background: #007BFF;
            color: white;
            border: none;
            padding: 15px;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background: #0056b3;
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group:last-child {
            margin-bottom: 0;
        }
        .additional-units {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
    </style>
</head>
<body>
    <form action="/submit" method="POST">
        <h2>Student Form</h2>
        <div class="form-group">
            <label for="reg_no">REG NO:</label>
            <input type="text" id="reg_no" name="reg_no" required>
        </div>
        <div class="form-group">
            <label for="name">NAME:</label>
            <input type="text" id="name" name="name" required>
        </div>
        <div class="form-group">
            <label for="gender">GENDER:</label>
            <select id="gender" name="gender" required>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
            </select>
        </div>
        <div class="form-group">
            <label for="age">AGE:</label>
            <input type="number" id="age" name="age" required>
        </div>
        <div class="form-group">
            <label for="address">ADDRESS:</label>
            <input type="text" id="address" name="address" required>
        </div>
        <div class="form-group">
            <label for="email">EMAIL:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
            <label for="course">COURSE:</label>
            <input type="text" id="course" name="course" required>
        </div>
        <div class="form-group">
            <label for="semester">SEMESTER:</label>
            <input type="text" id="semester" name="semester" required>
        </div>
        <div class="form-group">
            <label for="year">YEAR:</label>
            <input type="text" id="year" name="year" required>
        </div>
        <div class="form-group">
            <label for="course_units">COURSE UNITS:</label>
            <div class="additional-units">
                <input type="text" id="course_units" name="course_units" required>
                <input type="text" name="course_units_additional" maxlength="40">
                <input type="text" name="course_units_additional" maxlength="40">
                <input type="text" name="course_units_additional" maxlength="40">
                <input type="text" name="course_units_additional" maxlength="40">
            </div>
        </div>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
</html>
"""

@app.route('/')
def home():
    return render_template_string(index_html)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    # Here you could process/store the form data (e.g., save to a database)
    return render_template_string(success_html, name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)