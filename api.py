# app.py
from fastapi import FastAPI
import uvicorn
from Calc import Calc

# Create an instance of the FastAPI application
app = FastAPI(title="Biometric Users",
              description="System for managing users and roles with API Gateway for access control to another microservices",
              docs_url="/docs", )

calc = Calc()

# Define a route
# @app.get("/")
# def read_root():
#     return {"message": "Привет, Мир!"}

@app.post("/")
def add_expense(category: str, ammount: float, date: str):
    calc.add_expense(category, ammount, date)
    return {"message": "Расход добавлен!"}

@app.get("/")
def show_expense():
    calc.show_expense()
    return calc.show_expense()

@app.get("/analyze/")
def analyze_expenses():
    #calc.analyze_expenses()
    return calc.analyze_expenses()

if __name__ == '__main__':  #блок всегда! в конце
    uvicorn.run(
        'api:app',
        host='0.0.0.0',
        port=8001,
        reload=True,
        workers=1,
    )
