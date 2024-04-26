from drf_spectacular.extensions import OpenApiAuthenticationExtension


class JWTAuthenticationScheme(OpenApiAuthenticationExtension):

    target_class = "apps.users.authentication.JWTAuthentication"
    name = "JWTAuthentication"

    def get_security_definition(self, auto_schema):

        return {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "This endpoint requires JWT authentication.",
        }
