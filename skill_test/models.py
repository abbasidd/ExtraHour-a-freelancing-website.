from freelancer import models as f_model
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
class Quiz(models.Model):
    name = models.CharField(max_length=1000)
    questions_count = models.IntegerField(default=0)
    description = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    #roll_out = models.BooleanField(default=False)
    class Meta:
        ordering = ['created',]
        verbose_name_plural ='Quizzes'
    def __str__(self):
        return self.name
class Choice(models.Model):
    choice1 = models.CharField(max_length = 255)
    choice2 = models.CharField(max_length = 255)
    choice3 = models.CharField(max_length = 255)



class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    label = models.CharField(max_length=1000)
    order = models.IntegerField(default=0)
    choice =  models.OneToOneField(Choice, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000)
    def __str__(self):
        return self.label



class QuizTakers(models.Model):
    freelancer = models.ForeignKey(f_model.Freelancer, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correct_answers = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.freelancer.user.username

class user_answer(models.Model):
    quizTakers = models.ForeignKey(QuizTakers,on_delete=models.CASCADE)
    question = models.OneToOneField(Question, on_delete=models.SET_NULL,null=True)
    choice = models.CharField(max_length = 10)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.choice

@receiver(post_save, sender=Quiz)
def set_default_quiz(sender, instance, created,**kwargs):
    quiz = Quiz.objects.filter(id = instance.id)
    quiz.update(questions_count=instance.question_set.filter(quiz=instance.pk).count())
@receiver(post_save, sender=Question)
def set_default(sender, instance, created,**kwargs):
    quiz = Quiz.objects.filter(id = instance.quiz.id)
    quiz.update(questions_count=instance.quiz.question_set.filter(quiz=instance.quiz.pk).count())
