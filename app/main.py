from fastapi import FastAPI


def create_application():
    application = FastAPI()
    return application


app = create_application()


@app.get("/")
async def root():
    return {"message": "Hi, I am Shiva. Awesome - Your sertup is done & working."}