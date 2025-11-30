from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from authApp.permissions import RolePermission  
from .serializers import VehicleSerializer
from .models import VehicleModel
from authApp.views import CsrfExemptSessionAuthentication

# Create your views here.


class VehicleView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated,RolePermission]

    

    
    def get(self,request,vehicle_id=None):
        try:
            if vehicle_id is None:
                vehicles = VehicleModel.objects.all()
                serializer = VehicleSerializer(vehicles, many=True)
                return Response(
                    {
                        "success": True,
                        "status_code": status.HTTP_200_OK,
                        "message": "Vehicles retrieved successfully",
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            else:
                vehicle = VehicleModel.objects.get(id=vehicle_id)
                serializer = VehicleSerializer(vehicle)
                return Response(
                    {
                        "success": True,
                        "status_code": status.HTTP_200_OK,
                        "message": "Vehicle retrieved successfully",
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
        except VehicleModel.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "message": "Vehicle not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "An unexpected error occurred",
                    "errors": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    


            
    def post(self, request):
        try:
            serializer = VehicleSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "success": True,
                        "status_code": status.HTTP_201_CREATED,
                        "message": "Vehicle created successfully"
                    },
                    status=status.HTTP_201_CREATED
                )
            
            return Response(
                {
                    "success": False,
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "Vehicle creation failed",
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "An unexpected error occurred",
                    "errors": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

    def put(self,request,vehicle_id):
        try:
            vehicle = VehicleModel.objects.get(id=vehicle_id)
            serializer = VehicleSerializer(vehicle,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "success": True,
                        "status_code": status.HTTP_201_CREATED,
                        "message": "Vehicle updated successfully"
                    },
                    status=status.HTTP_201_CREATED
                )
            return Response(
                {
                    "success": False,
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "Vehicle creation failed",
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "An unexpected error occurred",
                    "errors": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

    def delete(self,request,vehicle_id):
        try:
            vehicle = VehicleModel.objects.get(id=vehicle_id)
            vehicle.delete()

            return Response(
                {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Vehicle deleted successfully"
                },
                status=status.HTTP_200_OK
            )
        except VehicleModel.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "message": "Vehicle not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "An unexpected error occurred",
                    "errors": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    