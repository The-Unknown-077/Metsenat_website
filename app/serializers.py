from rest_framework import serializers
from . import models


class SponsorSerializer(serializers.ModelSerializer):
    spent_amount = serializers.SerializerMethodField()

    def get_spent_amount(self, obj):
        from django.db.models import Sum
        sponsor_spent_amounts = obj.studentsponsor_set.aggregate(
            total_amount = Sum('amount')
        )['total_amount']
        return sponsor_spent_amounts

    class Meta:
        model = models.Sponsor
        fields = ('full_name', 'phone_number', 'donation_amout',
                  'org_name', 'type', 'spent_amount')



class SponsorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sponsor
        exclude = ('type', 'org_name', 'payment_type')


class StudentSponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudentSponsor
        fields = '__all__'

    def validate(self, attrs):
        amount = attrs ['amount']
        student = attrs ['student']
        sponsor = attrs ['sponsor']
        from django.db.models import Sum

        #1 - sponsor amounti yetadimi?
        sponsor_amount = sponsor.donation_amout
        sponsor_spent_money = models.StudentSponsor.objects.filter(sponsor=sponsor).aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        difference = sponsor_amount - sponsor_spent_money
        if sponsor_amount - sponsor_spent_money < amount:
            raise serializers.ValidationError(
                detail={'error': f'Bu homiyda {difference} som pul qolgan, bundan kop pul bera olmaysiz'}
            )

        return attrs



class SponsorUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sponsor
        exclude = ('id', 'created_at')


