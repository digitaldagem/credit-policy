from django.http import JsonResponse
from ..storage.credit_policy import CreditPolicy
from ..storage.serializers import CreditPolicySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..service.policy_check import checkPolicy

@api_view()
def get_credit_policies(request):
        creditPolicies = CreditPolicy.objects.all()
        serializer = CreditPolicySerializer(creditPolicies, many=True)
        return JsonResponse({"response": serializer.data}, safe=False)

@api_view(['POST'])
def post_credit_policy(request):
    serializer = CreditPolicySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        creditPolicy = serializer.save()
        result = checkPolicy(creditPolicy)
        if result == 'ACCEPT':
            return Response({"response": result}, status=status.HTTP_201_CREATED)
        else:
            creditPolicy.delete()
            return Response({"response": result}, status=status.HTTP_200_OK)
