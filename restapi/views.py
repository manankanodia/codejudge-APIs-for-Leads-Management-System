# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError, server_error

from restapi.models import Lead
from restapi.serializers import LeadSerializer


def get_object(pk):
    if not pk:
        raise ValidationError({
            "status": "failure",
            "reason": "lead_id is required"
        })
    try:
        return Lead.objects.get(pk=pk)
    except Lead.DoesNotExist:
        raise NotFound({})
    except Exception as err:
        raise server_error({"status": "failure", "reason": str(err)})


class Leads(APIView):
    """
        Retrieve, insert, update or delete a lead instance.
    """

    def get(self, request, pk=None):
        lead = get_object(pk)
        serializer = LeadSerializer(lead)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = LeadSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response({
                "status": "failure",
                "reason": str(err)
            }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        lead = get_object(pk)
        try:
            serializer = LeadSerializer(lead, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Exception as err:
            return Response({
                "status": "failure",
                "reason": str(err)
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        lead = get_object(pk)
        try:
            lead.delete()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except Exception as err:
            raise server_error({"status": "failure", "reason": str(err)})


class MarkLead(APIView):

    def put(self, request, pk=None):
        if "communication" not in request.data:
            return Response({
                "status": "failure",
                "reason": "communication key is required"
            }, status=status.HTTP_400_BAD_REQUEST)
        lead = get_object(pk)
        try:
            lead.status = 'Contacted'
            lead.communication = request.data.get('communication')
            lead.save()
            serializer = LeadSerializer(lead)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Exception as err:
            return Response({
                "status": "failure",
                "reason": str(err)
            }, status=status.HTTP_400_BAD_REQUEST)
