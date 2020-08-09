from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import reconstructor, relationship

from app.models.base import Base


class History(Base):
    id = Column(Integer, primary_key=True)
    root_qid = Column(Integer, ForeignKey('question.id'))
    qid = Column(Integer, ForeignKey('history_question.id'))
    student_aid = Column(Integer, ForeignKey('history_answer.id'))
    teacher_aid = Column(Integer, ForeignKey('history_answer.id'))
    root_question = relationship('Question', foreign_keys=root_qid, backref='history')
    question = relationship('HistoryQuestion', foreign_keys=qid)
    teacher_answer = relationship('HistoryAnswer', foreign_keys=teacher_aid)
    student_answer = relationship('HistoryAnswer', foreign_keys=student_aid)

    @staticmethod
    def create_from_question(history_question):
        lastHistory = History.query.order_by(-History.id).filter_by(root_question=history_question).first()
        history = History()
        history.root_question = history_question
        history.question = HistoryQuestion.copy_from(history_question)
        history.teacher_answer = lastHistory.teacher_answer if lastHistory else None
        history.student_answer = lastHistory.student_answer if lastHistory else None
        return history

    #
    @staticmethod
    def create_from_student_answer(history_answer):
        lastHistory = History.query.order_by(-History.id).filter_by(
            root_question=history_answer.question_from_student).first()
        history = History()
        history.root_question = history_answer.question_from_student
        history.question = lastHistory.question if lastHistory else None
        history.student_answer = HistoryAnswer.copy_from(history_answer)
        history.teacher_answer = lastHistory.teacher_answer if lastHistory else None
        return history

    @staticmethod
    def create_from_teacher_answer(history_answer):
        lastHistory = History.query.order_by(-History.id).filter_by(
            root_question=history_answer.question_from_teacher).first()
        history = History()
        history.root_question = history_answer.question_from_teacher
        history.question = lastHistory.question if lastHistory else None
        history.student_answer = lastHistory.student_answer if lastHistory else None
        history.teacher_answer = HistoryAnswer.copy_from(history_answer)
        return history

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['question', 'teacher_answer', 'student_answer']
        self.update_time = self.create_time


class HistoryQuestion(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(127), nullable=False)
    content = Column(Text, nullable=False)
    author_gid = Column(String(10), ForeignKey('user.gid'))
    author = relationship('User')

    @staticmethod
    def copy_from(question):
        historyQuestion = HistoryQuestion()
        for field in question.dump_fields:
            setattr(historyQuestion, field, getattr(question, field))
        return historyQuestion

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['id', 'title', 'content', 'author']
        self.update_time = self.create_time


class HistoryAnswer(Base):
    id = Column(Integer, primary_key=True)
    content = Column(String(500), nullable=False)
    author_gid = Column(String(10), ForeignKey('user.gid'))
    author = relationship('User')

    @staticmethod
    def copy_from(answer):
        historyAnswer = HistoryAnswer()
        for field in answer.dump_fields:
            setattr(historyAnswer, field, getattr(answer, field))
        return historyAnswer

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['id', 'content', 'author']
        self.update_time = self.create_time
