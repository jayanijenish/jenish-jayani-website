from flask import Flask, render_template
app = Flask(__name__)

jobs=[
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Mountain View, CA",
    "salary": "$120,000"
  },
  
  {
    "id": 2,
    "title": "Software Engineer",
    "location": "San Francisco, CA",
    "salary": "$120,000"
  },
  
  {
    "id": 3,
    "title": "Data Scientist",
    "location": "New York, NY",
    "salary": "$120,000"
  },
  
  {
    "id": 4,
    "title": "Data Engineer",
    "location": "Los Angeles, CA",
    "salary": "$120,000"
  },
]

@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=jobs,
                        company_name="om")
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
