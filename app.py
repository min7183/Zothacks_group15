from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import api_interact


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/items", response_class=HTMLResponse)
def read_item(request: Request, search_string: str, keyword_string: str):
    #pictures = zip(api_interact.get_items(api_interact.get_all(search_string, media = 'image')[0]).json())
    if keyword_string != '':
        pictures1 = api_interact.get_items(api_interact.get_all(search_string, keywords=keyword_string).json())[0]
        pictures2 = api_interact.get_items(api_interact.get_all(search_string, keywords=keyword_string).json())[1]
        zip(pictures1, pictures2) 
        return templates.TemplateResponse("item.html", {"request": request, "search_string": zip(pictures1, pictures2)})
    pictures1 = api_interact.get_items(api_interact.get_all(search_string).json())[0]
    pictures2 = api_interact.get_items(api_interact.get_all(search_string).json())[1]
    zip(pictures1, pictures2) 
    return templates.TemplateResponse("item.html", {"request": request, "search_string": zip(pictures1, pictures2)})
