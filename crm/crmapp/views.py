from rest_framework import viewsets, generics, mixins
from .models import Company, Speciality, Employee, Friendship
from .serializers import CompanySerializer, SpecialitySerializer, EmployeeSerializer, FriendshipSerializer
from django_filters import rest_framework as filters

class CompanyListView(viewsets.GenericViewSet,
                      viewsets.mixins.ListModelMixin,
                      viewsets.mixins.CreateModelMixin,
                      viewsets.mixins.RetrieveModelMixin,
                      viewsets.mixins.UpdateModelMixin,
                      viewsets.mixins.DestroyModelMixin):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class FriendshipView(viewsets.GenericViewSet,
                     viewsets.mixins.ListModelMixin,
                     viewsets.mixins.CreateModelMixin,
                     viewsets.mixins.RetrieveModelMixin,
                     viewsets.mixins.UpdateModelMixin,
                     viewsets.mixins.DestroyModelMixin):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class SpecialityListView(viewsets.GenericViewSet,
                  viewsets.mixins.ListModelMixin,
                  viewsets.mixins.CreateModelMixin,
                  viewsets.mixins.RetrieveModelMixin,
                  viewsets.mixins.UpdateModelMixin,
                  viewsets.mixins.DestroyModelMixin):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EmployeeListView(viewsets.GenericViewSet,
                  viewsets.mixins.ListModelMixin,
                  viewsets.mixins.CreateModelMixin,
                  viewsets.mixins.RetrieveModelMixin,
                  viewsets.mixins.UpdateModelMixin,
                  viewsets.mixins.DestroyModelMixin):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('company', 'speciality',)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
