from flask import Flask, render_template_string

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
            font-family: Arial, sans-serif;
            margin: 60px;
            padding: 30px;
            background-color:'white';

        }
        form {
            background: #fff;
            padding: 100px;
            border-radius: 0px;
            box-shadow: 0 0 5px #ccc;
            max-width: 800px;
           
        }
        input, select {
            width: 100%;
            padding: 20px;
            margin: 2px 0;
            border: 2px solid #ccc;
            border-radius: 5px;
           
        }
        button {
            background: #007BFF;
            color: white;
            border: none;
            padding: 20px;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <h2>Student Form</h2>
    <form action="process_form.php" method="POST">
        <label for="reg_no">REG NO:</label>
        <input type="text" id="reg_no" name="reg_no" required>

        <label for="name">NAME:</label>
        <input type="text" id="name" name="name" required>

        <label for="gender">GENDER:</label>
        <select id="gender" name="gender" required>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
        </select>

        <label for="age">AGE:</label>
        <input type="number" id="age" name="age" required>

        <label for="address">ADDRESS:</label>
        <input type="text" id="address" name="address" required>

        <label for="email">EMAIL:</label>
        <input type="email" id="email" name="email" required>

        <label for="course">COURSE:</label>
        <input type="text" id="course" name="course" required>

        <label for="semester">SEMESTER:</label>
        <input type="text" id="semester" name="semester" required>

        <label for="year">YEAR:</label>
        <input type="text" id="year" name="year" required>

        <label for="course_units">COURSE UNITS:</label>
        <input type="text" id="course_units" name="course_units" required>
        <input type="text" name="COURSE_UNITS" size="0" maxlength="40"style="float: center;"><br>
            <br>
            <input type="text" name="COURSE_UNITS" size="0" maxlength="40"style="float: center;"><br>
            <br>
            <input type="text" name="COURSE_UNITS" size="0" maxlength="40"style="float: center;"><br>
            <br>
            <input type="text" name="COURSE_UNITS" size="0" maxlength="40"style="float: center;"><br>
            <br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(index_html)

if __name__ == '__main__':
    app.run(debug=True)
