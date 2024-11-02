from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


#This is essential, instead of having to write jinja2templates everytime,
# it simplifies it to "templates"
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse) # Defines a route for the root URL ("/") that responds with HTML content.
async def read_root(request: Request):
    # Renders and returns the "index.html" template, passing the request object so it can be used in the template.
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login")
async def root():
    return {"message": "Hello, FastAPI!"}
