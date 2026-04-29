from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    priority: str = "Medium" 
    is_completed: bool = False

tasks_db: List[Task] = []
archive_db: List[Task] = []

# Вспомогательная функция для сортировки
def get_priority_weight(priority: str) -> int:
    weights = {"High": 0, "Medium": 1, "Low": 2}
    return weights.get(priority, 3)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Сортируем список перед отправкой в шаблон
    # Сначала по весу важности, затем по ID (чтобы новые были выше при равной важности)
    sorted_tasks = sorted(tasks_db, key=lambda x: (get_priority_weight(x.priority), x.id))
    
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "tasks": sorted_tasks, 
        "archived_tasks": archive_db
    })

@app.post("/add")
async def add_task(
    title: str = Form(...), 
    description: str = Form(None), 
    priority: str = Form("Medium")
):
    new_id = len(tasks_db) + len(archive_db) + 1
    new_task = Task(id=new_id, title=title, description=description, priority=priority)
    tasks_db.append(new_task)
    return RedirectResponse(url="/", status_code=303)

@app.post("/complete/{task_id}")
async def complete_task(task_id: int):
    global tasks_db
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            completed_item = tasks_db.pop(i)
            completed_item.is_completed = True
            # В архиве обычно сортировка не нужна (идут по порядку выполнения)
            archive_db.insert(0, completed_item) 
            break
    return RedirectResponse(url="/", status_code=303)