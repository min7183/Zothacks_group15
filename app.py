from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home_page(request: Request, id: str):
    return templates.TemplateResponse("item.html")


@app.get("/items/{id}", response_class=HTMLResponse)
def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})