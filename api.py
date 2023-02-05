from fastapi import FastAPI
app = FastAPI()


from router.mc import router as mc

prefix = "/api/v1"

app.include_router(mc, prefix=prefix)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level='info')

