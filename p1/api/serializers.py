from rest_framework.serializers import ModelSerializer
from p1.models import ControleOficio


class ControleOficioSerializer(ModelSerializer):
    class Meta:
        model = ControleOficio
        fields = ('id','numero','data', 'destino', 'assunto', 'responsavel')