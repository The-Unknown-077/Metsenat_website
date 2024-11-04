from django.shortcuts import render
from rest_framework import generics
from . import models, serializers
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.views import Response
from django.utils import timezone


class SponsorCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.SponsorSerializer

class SponsorListAPIView(generics.ListAPIView):
    serializer_class = serializers.SponsorListSerializer
    queryset = models.Sponsor.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['full_name']
    filterset_fields = ['status', 'donation_amout', 'created_at']


class SponsorDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.SponsorListSerializer
    queryset = models.Sponsor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.SponsorListSerializer
        return serializers.SponsorUpdateSerializer


class CreateStudentSponsorAPIView(generics.CreateAPIView):
    serializer_class = serializers.StudentSponsorSerializer





class StatisticNumberAPIView(APIView):

    def get(self, request):
        approwed_amount = models.StudentSponsor.objects.all().aggregate(total_amount=Sum('amount'))['total_amount']
        requested_amount = models.Student.objects.aggregate(total=Sum('contract_amount'))['total']
        return Response({
            "approved_amount": approwed_amount,
            "requested_amount": requested_amount
        })


class GraphAPIView(APIView):

    def get(self, request):
        this_year = timezone.now().year

        students = models.Student.objects.filter(created_at__year=this_year)
        sponsors = models.Sponsor.objects.filter(created_at__year=this_year)

        result = []
        for i in range(1,13):
            result.append({
                'students_count': students.filter(created_at__month=i).count(),
                'sponsors_count': sponsors.filter(created_at__month=i).count()
            })
        return Response(result)






