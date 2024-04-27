from rest_framework.serializers import Serializer
from rest_framework import generics
from typing import List, Callable


class MappedAPIView(generics.GenericAPIView):
    """
    A base view class that maps HTTP methods to specific application classes,
    authentication classes, permission classes, and serializers.

    The mappings allow different behavior for different HTTP methods in the same view.
    For example, you might want to use different serializers for GET and POST requests,
    or apply different permissions for different methods.

    #### Attributes:
    - application_class: class that represents the use case to be used in the view.
    - application_mapping: A dictionary that maps different use cases to the view's
    HTTP methods.
    - authentication_mapping: A dictionary that maps authentication classes to the
    view's HTTP methods.
    - permission_mapping: A dictionary that maps permission classes to the view's
    HTTP methods.
    - serializer_mapping: A dictionary that assigns serializers to the view's HTTP
    methods.
    """

    application_class = None
    application_mapping = {}
    authentication_mapping = {}
    permission_mapping = {}
    serializer_mapping = {}

    def get_authenticators(self):
        """
        Instantiates and returns the list of authenticators that this view can use.
        """

        try:
            authentication_classes = self.authentication_mapping[
                self.request.method
            ]
        except AttributeError:
            authentication_classes = []

        return [auth() for auth in authentication_classes]

    def get_permissions(self) -> List:
        """
        Get the permissions based on the request method.
        """

        try:
            permission_classes = self.permission_mapping[self.request.method]
        except KeyError:
            raise ValueError(f"Method {self.request.method} not allowed")

        return [permission() for permission in permission_classes]

    def get_serializer_class(self) -> Serializer:
        """
        Get the serializer class based on the request method.
        """

        try:
            serializer = self.serializer_mapping[self.request.method]
        except KeyError:
            raise ValueError(f"Method {self.request.method} not allowed")

        return serializer

    def get_application_class(self) -> Callable:
        """
        Get the application class based on the request method.
        """

        try:
            application_class = self.application_mapping[self.request.method]
        except KeyError:
            raise ValueError(f"Method {self.request.method} not allowed")

        return application_class
