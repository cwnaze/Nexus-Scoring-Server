from fastapi import FastAPI
import mysql.connector
from dotenv import load_dotenv
import os

mydb = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASS"),
  database=os.getenv("DB_NAME")
)

mycursor = mydb.cursor()

app = FastAPI()

@app.get('/check')
async def check_flag(challenge: str, flag: str):
    mycursor.execute('SELECT points FROM flags where challenge = %s and flag = %s', (challenge, flag))
    points = mycursor.fetchall()
    if points:
        return points[0][0]
    return 0

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
