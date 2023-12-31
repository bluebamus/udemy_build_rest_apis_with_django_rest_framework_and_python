from rest_framework import serializers
from watchlist_app.models import Movie
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    # review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ("watchlist",)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source="platform.name")

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    # class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist1 = serializers.StringRelatedField(
    #     many=True,
    #     source="watchlist",
    # )
    # watchlist2 = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=True,
    #     source="watchlist",
    # )
    # watchlist3 = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name="movie-details",
    #     source="watchlist",
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"

        # extra_kwargs = {
        #     "url": {
        #         "view_name": "stream-detail"
        #     },  # Replace 'custom-model-detail' with your desired view name
        # }


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")


# class MovieSerializer(serializers.Serializer):
# class MovieSerializer(serializers.ModelSerializer):

#  class Meta:
#      model = Movie
#      fields = "__all__"
#      fields = ['id','name','description']
#      exclude = ['active']

#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError(
#                 "Title and Description should be different!"
#             )
#         else:
#             return data

#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
#         else:
#             return value
