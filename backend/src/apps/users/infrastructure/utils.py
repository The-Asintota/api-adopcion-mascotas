from apps.users.domain.typing import JWToken, JWTPayload
from settings.environments.base import SIMPLE_JWT
from jwt import decode
from typing import Dict


def decode_jwt(token: JWToken, options: Dict[str, bool] = None) -> JWTPayload:

    return decode(
        jwt=token,
        key=SIMPLE_JWT["SIGNING_KEY"],
        algorithms=[SIMPLE_JWT["ALGORITHM"]],
        options=options,
    )
