from django.db import models

# Create your models here.
# subject : 질문의 제족
# content : 질문의 내용
# create_date : 질문을 작성한 일시

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
    pass



# question : 질문
# content : 답변의 내용
# create_date : 답변을 작성한 일시
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    pass


# 질문 항목과 답변 항목 만들기
# ORM
