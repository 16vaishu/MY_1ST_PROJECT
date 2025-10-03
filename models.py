from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Topics table
class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    quizzes = relationship("Quiz", back_populates="topic")

# Quizzes table
class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id"))

    topic = relationship("Topic", back_populates="quizzes")
    submissions = relationship("Submission", back_populates="quiz")

# Submissions table
class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String)
    score = Column(Integer)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))

    quiz = relationship("Quiz", back_populates="submissions")
