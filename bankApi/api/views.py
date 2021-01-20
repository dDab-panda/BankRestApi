from django.shortcuts import render 
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from django.db import connection, transaction

from .models import Bank
from .serializers import ApiSerializer



class BranchesApiView(ListAPIView):
    serializer_class = ApiSerializer

    def get_queryset(self,*args,**kwargs):
        header1 = self.request.GET.get("q")
        header2 = self.request.GET.get("limit")
        header3 = self.request.GET.get("offset")

        if header1 is None:
            header1 = ""

        if header2 is None or header2 == "" or header3 is None or header3 == "":
            no_selection=[]
            return no_selection

        query = "Select * from bank_branches where branch like '%"+header1+"%' ORDER BY ifsc Limit "+header2+" OFFSET "+header3           
        cursor = connection.cursor()
        cursor.execute(query)
        transaction.commit()
        query_response = cursor.fetchall()

        bank_response_list = []

        for i in query_response:
            bank_item = Bank(ifsc = i[0],bank_id = i[1],branch = i[2], address = i[3], city = i[4],district = i[5], state = i[6])
            bank_response_list.append(bank_item)
        
        return bank_response_list

    def list(self, request, *args, **kwargs):
        header2 = self.request.GET.get("limit")
        header3 = self.request.GET.get("offset")
        if header2 is None or header2 == "" or header3 is None or header3 == "":
            return HttpResponse(status=400)

        queryset = self.get_queryset()
        serializer = ApiSerializer(list(queryset),many=True)
        return Response(serializer.data)        

class BankApiView(ListAPIView):
    serializer_class = ApiSerializer

    def get_queryset(self,*args,**kwargs):
        header1 = self.request.GET.get("q")
        header2 = self.request.GET.get("limit")
        header3 = self.request.GET.get("offset")

        if header1 is None:
            header1 = ""

        if header2 is None or header2 == "" or header2 is None or header3 == "":
            no_selection=[]
            return no_selection

        query = "Select * from bank_branches where ifsc like '%"+header1+"%' OR branch like '%"+header1+"%' OR address like '%"+header1+"%' OR city like '%"+header1+"%' OR district like '%"+header1+"%' OR state like '%"+header1+"%' ORDER BY ifsc Limit "+header2+" OFFSET "+header3           
        cursor = connection.cursor()
        cursor.execute(query)
        transaction.commit()
        query_response = cursor.fetchall()

        bank_response_list = []

        for i in query_response:
            bank_item = Bank(ifsc = i[0],bank_id = i[1],branch = i[2], address = i[3], city = i[4],district = i[5], state = i[6])
            bank_response_list.append(bank_item)
        
        return bank_response_list

    def list(self, request, *args, **kwargs):
        header2 = self.request.GET.get("limit")
        header3 = self.request.GET.get("offset")
        if header2 is None or header2 == "" or header3 is None or header3 == "":
            return HttpResponse(status=400)

        queryset = self.get_queryset()
        serializer = ApiSerializer(list(queryset),many=True)
        return Response(serializer.data)        