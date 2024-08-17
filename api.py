from fastapi import FastAPI
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)

mycursor = mydb.cursor()

app = FastAPI()

@app.get('/check')
async def check_flag(challenge: str, flag: str, ip: str):
    # Query for points based on challenge and flag
    mycursor.execute('SELECT points FROM flags WHERE challenge = %s AND flag = %s', (challenge, flag))
    points = mycursor.fetchone()  # Use fetchone() to get a single row
    
    # Query for team_name based on IP address
    mycursor.execute('SELECT team_name FROM team_challenge WHERE ip_address = %s', (ip,))
    team_name = mycursor.fetchone()  # Use fetchone() to get a single row
    
    # Check if points were found
    if points and team_name:
        return {"points": points[0], "team_name": team_name[0]}
    
    return {"points": 0, "team_name": None}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
