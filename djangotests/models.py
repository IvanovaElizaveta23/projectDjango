from django.contrib.auth.models import User
from django.db import models


class Difficultion(models.Model):
    name = models.CharField(max_length=255, verbose_name='Уровень сложности')

    class Meta:
        verbose_name = "Уровень сложности"
        verbose_name_plural = "Уровни сложности"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Test(models.Model):
    # cover = models.ImageField(upload_to='images/', blank=True, verbose_name="Обложка теста")
    name = models.CharField(max_length=255, verbose_name='Название')
    time_limit = models.TimeField(verbose_name='Время прохождения')
    quantity_attempts = models.IntegerField(null=True, verbose_name='Количество попыток')
    cat = models.ForeignKey('Category', related_name='tests', on_delete=models.CASCADE, verbose_name="Категория")
    dif = models.ForeignKey('Difficultion', related_name='tests', on_delete=models.CASCADE, verbose_name="Уровень сложности")

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self):
        return self.name


class Question(models.Model):
    content = models.CharField(max_length=255, verbose_name='Вопрос')
    test = models.ForeignKey('Test', related_name='questions', on_delete=models.CASCADE, verbose_name='Тест')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.content


class Answer(models.Model):
    content = models.CharField('Вариант ответа', max_length=255)
    right = models.BooleanField(verbose_name='Является правильным ответом')
    quest = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE, verbose_name='Идентификатор вопроса')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.content


class Session(models.Model):
    user = models.ForeignKey('auth.User', related_name='sessions', on_delete=models.CASCADE, verbose_name='Пользователь')
    test = models.ForeignKey('Test', on_delete=models.CASCADE, verbose_name='Тест')
    time_start = models.DateTimeField(auto_now_add=True, verbose_name='Начало прохождения теста')
    time = models.TimeField(null=True, verbose_name='Время прохождения')
    result = models.IntegerField(null=True, verbose_name='Результат теста')

    class Meta:
        verbose_name = "Сессия"
        verbose_name_plural = "Сессии"


class AnswerUser(models.Model):
    session = models.ForeignKey('Session', related_name='answersUser', on_delete=models.CASCADE, verbose_name='Сессия')
    ques = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name='Вопрос')
    answers = models.CharField('Ответы на тест', max_length=255)

    class Meta:
        verbose_name = "Ответ пользователя"
        verbose_name_plural = "Ответы пользователя"
