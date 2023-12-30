from fastapi import FastAPI


app = FastAPI()

@app.post('/login')
async def login():
    pass

@app.get('/all_entries')
async def retrieve_entries():
    pass