from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Topic, Quiz, Submission
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# ----- Create tables -----
Base.metadata.create_all(bind=engine)

# ----- FastAPI app -----
app = FastAPI(title="PySQL Gym API")

# ----- Pydantic Schemas -----
class TopicCreate(BaseModel):
    name: str

class QuizCreate(BaseModel):
    title: str
    topic_id: int

class SubmissionCreate(BaseModel):
    student_name: str
    score: int
    quiz_id: int

# ----- CRUD Endpoints -----
# Topics
@app.post("/topics/")
def create_topic(topic: TopicCreate, db: Session = Depends(get_db)):
    db_topic = Topic(name=topic.name)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic

@app.get("/topics/")
def get_topics(db: Session = Depends(get_db)):
    return db.query(Topic).all()

# Quizzes
@app.post("/quizzes/")
def create_quiz(quiz: QuizCreate, db: Session = Depends(get_db)):
    db_quiz = Quiz(title=quiz.title, topic_id=quiz.topic_id)
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz

@app.get("/quizzes/")
def get_quizzes(db: Session = Depends(get_db)):
    return db.query(Quiz).all()

# Submissions
@app.post("/submissions/")
def create_submission(sub: SubmissionCreate, db: Session = Depends(get_db)):
    db_sub = Submission(student_name=sub.student_name, score=sub.score, quiz_id=sub.quiz_id)
    db.add(db_sub)
    db.commit()
    db.refresh(db_sub)
    return db_sub

@app.get("/submissions/")
def get_submissions(db: Session = Depends(get_db)):
    return db.query(Submission).all()

# ----- UI Route for PySQL Gym -----
# Static files & templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    """
    Home page: PySQL Gym UI
    """
    return templates.TemplateResponse("index.html", {"request": request})
