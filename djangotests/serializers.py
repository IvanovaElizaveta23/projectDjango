from rest_framework import serializers

from .models import *


class AnswerUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerUser
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    answersUser = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Session
        fields = "__all__"
        read_only_fields = ('user', 'time_start', 'result')

    def update(self, instance, validated_data):
        instance.time = validated_data.get("time")

        result = 0
        for answerUser in AnswerUser.objects.filter(session=instance.id):
            # Получить ответы для вопроса
            answers = Answer.objects.filter(quest=answerUser.ques)
            # Получить ответы пользователя для вопроса из строки (заменить на id)
            answerUserList = [int(item) for item in answerUser.answers.split(",")]
            for i in range(answers.count()):
                if answers[i].right:
                    if i+1 in answerUserList:
                        result += 1

        instance.result = result
        instance.save()
        return instance


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='answer-detail')

    class Meta:
        model = Question
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # cat = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='cat.name')
    # dif = serializers.PrimaryKeyRelatedField(queryset=Difficultion.objects.all(), source='dif.name')

    class Meta:
        model = Test
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    tests = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"


class DifficultionSerializer(serializers.ModelSerializer):
    tests = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Difficultion
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    sessions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'sessions')
