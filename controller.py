from fastapi import Depends, FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from . import crud, schemas
from .database import get_connection

app = FastAPI()

# テンプレート関連の設定 (jinja2)
templates = Jinja2Templates(directory="app/templates")

# 静的ファイル(css,js etc..)マウント
app.mount("/static", app=StaticFiles(directory="app/static"), name="static")

# Dependency
def get_db():
    try:
        with get_connection() as connection:
            yield connection
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {e}")

# メニュー画面
@app.get("/")
def top(request: Request):
    return templates.TemplateResponse('top.html', {'request': request})

# 新規登録画面
@app.get("/register")
async def show_register_form(request: Request):
    return templates.TemplateResponse('register.html', {'request': request, 'username': '', 'error': []})

# 新規登録処理
@app.post("/register")
async def register(request: Request, db=Depends(get_db)):
    data = await request.form()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    # バリデーションのチェック
    error = []
    if not username:
        error.append('ユーザー名は必須です。')
    if not password:
        error.append('パスワードは必須です。')
    if not email:
        error.append('メールアドレスは必須です。')

    if error:
        return templates.TemplateResponse('register.html', {'request': request, 'username': username, 'error': error})

    # データベースに保存
    try:
        db_user = crud.get_user_by_email(db, email=email)
        if db_user:
            error.append('このメールアドレスは既に登録されています。')
            return templates.TemplateResponse('register.html', {'request': request, 'username': username, 'error': error})

        new_user = schemas.UserCreate(email=email, username=username, password=password)
        crud.create_user(db, user=new_user)
        return RedirectResponse(url='/top')
    except Exception as e:
        error.append('内部サーバーエラーが発生しました。')
        error.append(str(e))
        return templates.TemplateResponse('register.html', {'request': request, 'username': username, 'error': error})

@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db=Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
