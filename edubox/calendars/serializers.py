from rest_framework import serializers

from .models import Calendar, Event, Account, Membership

class CalendarSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="calendar:calendar-detail")

    class Meta:
        model = Calendar
        fields = ('id', 'name', 'isShareable')
    
    def create(self, validated_data):
        return Calendar.objects.create(**validated_data)

class EventSerializer(serializers.HyperlinkedModelSerializer):
    calendar = serializers.PrimaryKeyRelatedField(many=False, queryset=Calendar.objects.all())
    # calendar = serializers.HyperlinkedRelatedField(view_name='calendar:calendar-detail', read_only=True)

    class Meta:
        model = Event
        fields = ('eventId', 'calendar', 'title', 'date', 'time', 'content_type', 'duration', 'note')
        # fields = ('title', 'date', 'time', 'content_type', 'duration', 'note')
    
    # def to_representation(self, instance):
    #     self.fields['calendar'] =  CalendarSerializer(read_only=True)
    #     return super(EventSerializer, self).to_representation(instance)
        
class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username')

class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    # calendarId = serializers.PrimaryKeyRelatedField(read_only=True)
    # accountId = serializers.PrimaryKeyRelatedField(read_only=True)
    calendar = serializers.PrimaryKeyRelatedField(many=False, queryset=Calendar.objects.all())
    account = serializers.PrimaryKeyRelatedField(many=False, queryset=Account.objects.all())

    class Meta:
        model = Membership
        fields = ('id', 'calendar', 'account', 'isDeleted')
    
    def update(self, instance, validated_data):
        instance.isDeleted = validated_data.get('isDeleted', instance.isDeleted)
        instance.save()
        return instance