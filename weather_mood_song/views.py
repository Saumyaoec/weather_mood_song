from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInput
from .serializers import UserInputSerializer
from .utils import get_weather, get_song_recommendation

class InputMood(APIView):
    def post(self, request):
        serializer = UserInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MatchWeatherWithMood(APIView):
    def get(self, request):
        user_input = UserInput.objects.latest('id')
        weather = get_weather(user_input.city)
        
        mood = user_input.mood
        if weather:
            happy_conditions = ["Clear", "Clouds", "Haze"]
            sad_conditions = ["Rain", "Drizzle", "Thunderstorm"]

            if (mood == "Happy" and weather["weather"] in happy_conditions) or \
               (mood == "Sad" and weather["weather"] in sad_conditions):
                
                song_recommendation = get_song_recommendation(mood)

                if song_recommendation:
                    message = f"Matched mood with weather. Song recommendation: {song_recommendation['song']} by {song_recommendation['artist']}."
                else:
                    message = "Matched mood with weather, but couldn't find a song recommendation."
                
                return Response({"message": message})
            
            else:
                return Response({"message": "Weather doesn't match the mood."})
        else:
            return Response({"error": "City not found."}, status=status.HTTP_404_NOT_FOUND)
