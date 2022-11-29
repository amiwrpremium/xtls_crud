from .python import (
    inbound__get__python__sample,
    inbound__post__python__sample,
    builders__post__python__sample,
)
from .js import (
    inbound__get__js__sample,
    inbound__post__js__sample,
    builders__post__js__sample,
)
from .models import XCodeSample

inbound__get = XCodeSample(
    path="/api/v1/inbounds/",
    method="get",
    samples=[
        inbound__get__python__sample,
        inbound__get__js__sample,
        inbound__post__python__sample,
        inbound__post__js__sample,
    ]
)

builders__post = XCodeSample(
    path="/api/v1/builders/",
    method="post",
    samples=[
        builders__post__python__sample,
        builders__post__js__sample
    ]
)
