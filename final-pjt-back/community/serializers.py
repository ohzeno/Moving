from rest_framework import serializers
from .models import Review, Comment

class ReviewListSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()
  
    def get_userName(self,obj):
        return obj.user.username
    
    class Meta:
        model = Review
        fields = ('id', 'movie_title', 'title', 'userName', 'updated_at', 'movie')
        

class ReviewSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()
  
    def get_userName(self,obj):
        return obj.user.username
    
    class Meta:
        model = Review
        fields = ('id', 'userName', 'movie_title', 'title', 'content', 'rank', 'created_at', 'updated_at')
        read_only_fields = ('user', 'movie')
        
        
class CommentSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()
    
    def get_userName(self,obj):
        return obj.user.username
    
    class Meta:
        model = Comment
        fields = ('id', 'userName', 'content', 'created_at', 'updated_at')
        read_only_fields = ('user', 'review')

