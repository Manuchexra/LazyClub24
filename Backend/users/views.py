import logging
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework import generics, status
from .serializers import CreateUserSerializer, TestSerializer, ResultSerializer
from .tokens import account_activation_token
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Test , Result, Lesson2
from django.http import JsonResponse


logger = logging.getLogger(__name__)

class RegisterView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        logger.debug(f"Request data: {request.data}")
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user = response.data
            uid = urlsafe_base64_encode(force_bytes(user['id']))
            token = account_activation_token.make_token(user)
            activation_link = f"{settings.FRONTEND_URL}/activate?uid={uid}&token={token}"
            message = f"Iltimos havola orqali accountingizni faollashtiring!: {activation_link}"
            send_mail('Accountingizni faollashtiring', message, 'from@example.com', [user['email']])
        elif response.status_code == status.HTTP_400_BAD_REQUEST:
            logger.error(f"Errors: {response.data}")
        return response

class TestView(APIView):
    def get(self, request: Request, pk=None,q_type=None,q_subject=None) -> Response:
        if pk is None and q_subject is None and q_type is None:
            tests = Test.objects.all()
            serializer = TestSerializer(tests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif q_subject==None and q_type==None:
            try:
                test = Test.objects.get(pk=pk)
                serializer = TestSerializer(test)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Test.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif pk==None and q_subject==None:
            try:
                test = Test.objects.filter(question_type1=q_type)
                serializer = TestSerializer(test,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Test.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif pk==None:
            try:
                task = Test.objects.filter(question_type1=q_type,question_subject=q_subject)
                serializer = TestSerializer(task,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Test.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
def get_titles(request):
    lessons = Lesson2.objects.all().values('id', 'title')  # Select only id and title
    return JsonResponse(list(lessons), safe=False)

def get_lesson_details(request, lesson_id):
    try:
        lesson = Lesson2.objects.get(pk=lesson_id)
        data = {
            'id': lesson.id,
            'title': lesson.title,
            'information': lesson.information,
            'photo': lesson.photo  # Get the image URL
        }
        return JsonResponse(data)
    except Lesson2.DoesNotExist:
        return JsonResponse({'error': 'Lesson not found'}, status=404)
def get_all_lessons(request):
    lessons = Lesson2.objects.all()
    data = [{'title': lesson.title, 'photo': lesson.photo, 'information': lesson.information} for lesson in lessons]
    return JsonResponse(data, safe=False)