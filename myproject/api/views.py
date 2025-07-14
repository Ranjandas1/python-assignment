from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import WheelForm, WheelField
from .serializers import WheelFormSerializer, WheelFieldSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import WheelFormFilter


class WheelFormViewSet(viewsets.ModelViewSet):
    queryset = WheelForm.objects.all()
    serializer_class = WheelFormSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = WheelFormFilter
    http_method_names = ['get', 'post']


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        full_data = response.data
        filtered_data = {
            "formNumber": full_data.get("formNumber"),
            "submittedBy": full_data.get("submittedBy"),
            "submittedDate": full_data.get("submittedDate"),
            "status": "saved",
        }
        return Response({
            "message": "Wheel specification submitted successfully.",
            "success": True,
            "data": filtered_data,
        }, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        required_fields = ['formNumber', 'submittedBy', 'submittedDate']
        any_filter_provided = any(field in request.query_params for field in required_fields)

        if any_filter_provided:
            all_filters_present = all(
                request.query_params.get(field) not in [None, '']
                for field in required_fields
            )

            if not all_filters_present:
                return Response({
                    "success": False,
                    "message": "No data found for the given filters.",
                    "data": None
                }, status=status.HTTP_200_OK)

        queryset = self.filter_queryset(self.get_queryset())

        if any_filter_provided and not queryset.exists():
            return Response({
                "success": False,
                "message": "No data found for the given filters.",
                "data": None
            }, status=status.HTTP_200_OK)

        custom_data = []
        for form in queryset:
            try:
                wheel_field = form.fields
                fields_dict = {
                    "treadDiameterNew": wheel_field.treadDiameterNew,
                    "lastShopIssueSize": wheel_field.lastShopIssueSize,
                    "condemningDia": wheel_field.condemningDia,
                    "wheelGauge": wheel_field.wheelGauge,
                }
            except WheelField.DoesNotExist:
                fields_dict = {}

            custom_data.append({
                "formNumber": form.formNumber,
                "submittedBy": form.submittedBy,
                "submittedDate": form.submittedDate,
                "fields": fields_dict
            })

        if not custom_data:
            return Response({
                "success": False,
                "message": "No wheel specification found.",
                "data": None
            }, status=status.HTTP_200_OK)

        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": custom_data
        }, status=status.HTTP_200_OK)
