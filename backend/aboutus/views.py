from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import OurStory, CoreValue, Program, TeamMember
from .serializers import (
    OurStorySerializer,
    CoreValueSerializer,
    ProgramSerializer,
    TeamMemberSerializer,
)


class AboutUsAPIView(APIView):

    def get(self, request):
        story = OurStory.objects.first()
        core_values = CoreValue.objects.all()
        programs = Program.objects.all()
        team_members = TeamMember.objects.all()

        data = {
            "our_story": OurStorySerializer(story).data if story else None,
            "core_values": CoreValueSerializer(core_values, many=True).data,
            "programs": ProgramSerializer(programs, many=True).data,
            "team_members": TeamMemberSerializer(team_members, many=True).data,
        }

        return Response(data, status=status.HTTP_200_OK)