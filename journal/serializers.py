from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import JournalEntry

class JournalEntrySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    links = serializers.SerializerMethodField()

    class Meta:
        model = JournalEntry
        fields = [
            'id', 'author',
            'title', 'content',
            'mood', 'is_public', 'created_at',
            'links'
        ]
        read_only_fields = [
            'created_at',
        ]

    def get_links(self, obj):
        request = self.context.get('request')
        if not request:
            return []
        
        # O DefaultRouter gerou o basename 'journalentry', então as rotas são 'journalentry-detail', etc.
        url = reverse('journalentry-detail', kwargs={'pk': obj.pk}, request=request)
        
        return [
            {
                "rel": "self",
                "href": url,
                "method": "GET"
            },
            {
                "rel": "update",
                "href": url,
                "method": "PUT"
            },
            {
                "rel": "delete",
                "href": url,
                "method": "DELETE"
            }
        ]
