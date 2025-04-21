from rest_framework.decorators import api_view
from rest_framework.response import Response
# import pandas as pd
# import joblib
# import os


# model_path = os.path.join(os.path.dirname(__file__), '..', 'models', '#####model-name####.joblib')
# model = joblib.load(model_path)


@api_view(['GET'])
def root_view(request):
    return Response({"message": "Forecasting Service API"})

