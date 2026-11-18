from flask import Flask
import redis
import os

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    visits = redis_client.incr("visits")
    return f"""
    <h1>Docker Compose Application</h1>
    <p>Backend: Flask</p>
    <p>Database: Redis</p>
    <p>Total visits: {visits}</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
