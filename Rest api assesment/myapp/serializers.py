from rest_framework import serializers
from .models import Novel

class NovelSerializer(serializers.ModelSerializer):
	class Meta:
		model=Novel
		fields=('id','title','content','created_at','updated_at')