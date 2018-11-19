from rest_framework.viewsets import ModelViewSet
from p1.models import ControleOficio
from .serializers import ControleOficioSerializer

class ControleOficioViewSet(ModelViewSet):
    queryset = ControleOficio.objects.all()
    serializer_class = ControleOficioSerializer