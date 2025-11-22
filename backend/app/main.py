from fastapi import FastAPI

app = FastAPI(title="Steam Wishlist Recommender API")


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}
