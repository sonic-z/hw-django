# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView

from .models import Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer


class CreateMeasurementView(CreateAPIView):
    serializer_class = MeasurementSerializer


class LCRUSensorsView(ListCreateAPIView, RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        print(self.kwargs)
        if 'pk' in str(self.kwargs):
            return Sensor.objects.filter(id=self.kwargs['pk'])
        else:
            return Sensor.objects.all().order_by('id')


