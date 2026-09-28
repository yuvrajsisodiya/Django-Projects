from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime
from time import perf_counter
# class SimpleMiddleware(MiddlewareMixin):
#     def process_reqeust(self,request):
#         print("This is Process Request")
#         print("request path : ",request.path)
#         print("request method : ",request.method)
#         print("Current Datetime : ",datetime.now())

#     def process_response(self,request,response):
#         print("This is Process Response")
#         print("Response status code : ",response.status_code)
#         print("Response time : ",datetime.now())
#         return response

# class MyMiddleware(MiddlewareMixin):
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         print("Request aayi")

#         response = self.get_response(request)

#         print("Response ja raha hai")

#         return response

# class RequestTimeMiddleware(MiddlewareMixin):
#     def process_request(self,request):
#         print("Request sent")
#         request.start_time = datetime.now()
#         print(f"Request to {request.path} started at {request.start_time}")
    
#     def process_response(self,request,response):
#         if hasattr(request , 'start_time'):
#            print("Response ")
#            end_time = datetime.now()
#            time_duration = end_time - request.start_time
#            print(f"Request to {request.path} ended at {end_time}")
#            print(f"Request to {request.path} took {time_duration.total_seconds()} seconds.")
#         return response

# class PerformanceMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         request.start_time = perf_counter()

#     def process_response(self, request, response):
#         if hasattr(request, 'start_time'):
#             end_time = perf_counter()
#             duration = end_time - request.start_time
#             print(f"Request to {request.path} took {duration:.4f} seconds.")
#         return response

# class BlockIPMiddleware(MiddlewareMixin):
#     def process_request(self,request):
#         ip_block='127.0.0.4'
#         user_ip = request.META.get('REMOTE_ADDR')
#         if user_ip == ip_block:
#             return HttpResponse("<p>YOUR IP address is Blocked </p>")

#         return None
class LoginCheckMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.path.startswith('/home/'):
            if not request.user.is_authenticated:
                return HttpResponse("<h1>You Must be logged in to access this page</h1>")
            return None