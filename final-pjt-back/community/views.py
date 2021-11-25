from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Review, Comment
from movies.models import Movie
# from .forms import ReviewForm, CommentForm
from .serializers import ReviewListSerializer, CommentSerializer, ReviewSerializer
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@api_view(['GET'])
@permission_classes([AllowAny])
def get_review_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def review_create(request):
    serializer = ReviewSerializer(data=request.data)
    # print(request.user)
    # print(request.data)
    movie = get_object_or_404(Movie, title=request.data['movie_title'])
    # print(request.data['movie_title'])
    # request.data['rank'] = float(request.data['rank'])
    # print(request.data)
    if serializer.is_valid(raise_exception=True):
        try:
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    if request.user.reviews.filter(pk=review_pk).exists():
        if request.method == 'DELETE':
            review.delete()
            data = {
                'deleted': f'{review_pk}번 리뷰가 성공적으로 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    return Response({'Unauthorized': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JSONWebTokenAuthentication])
def comment_list_or_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method=='GET':
        comments = review.comments.all()
        comments = comments.order_by('-pk')
        serializer= CommentSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        serializer = CommentSerializer(data=request.data)
        # print(request.user)
        # print(serializer)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save(user=request.user, review=review)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'DELETE'])  
def comment_update_or_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'DELETE':
            comment.delete()
            data = {
                'deleted' : f'{comment_pk}번 댓글이 성공적으로 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    return Response({ 'Unauthorized': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

