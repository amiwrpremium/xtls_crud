import typing as t

from pydantic import BaseModel, root_validator, validator


_Langs = t.Literal[
    "C",
    "C#",
    "C++",
    "CoffeeScript",
    "CSS",
    "Dart",
    "DM",
    "Elixir",
    "Go",
    "Groovy",
    "HTML",
    "Java",
    "JavaScript",
    "Kotlin",
    "Objective-C",
    "Perl",
    "PHP",
    "PowerShell",
    "Python",
    "Ruby",
    "Rust",
    "Scala",
    "Shell",
    "Swift",
    "TypeScript",
]

_Methods = t.Literal[
    "get",
    "post",
    "put",
    "patch",
    "delete",
    "head",
    "options",
    "connect",
    "trace",
]


class CodeSample(BaseModel):
    lang: _Langs
    label: t.Optional[str] = None
    source: str

    @root_validator()
    def set_label(cls, values):
        if not values.get("label"):
            values["label"] = values["lang"]
        return values

    @root_validator()
    def strip_source(cls, values):
        values["source"] = values["source"].strip()
        return values


class XCodeSample(BaseModel):
    path: str
    method: _Methods
    samples: t.List[CodeSample]

    @validator("method")
    def method_to_lower(cls, v):
        return v.lower()

    @validator("path")
    def start_and_end_with_slash(cls, v):
        if not v.startswith("/"):
            v = "/" + v
        if not v.endswith("/"):
            v = v + "/"
        return v

    @property
    def samples_dict_list(self) -> list:
        return [x.dict() for x in self.samples]

    @property
    def samples_json_list(self) -> list:
        return [x.json() for x in self.samples]
