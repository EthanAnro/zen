from typing import Any, Optional, TypedDict
from collections.abc import Awaitable

class EvaluateResponse(TypedDict):
    performance: str
    result: dict
    trace: dict

class ZenEngine:
    def __init__(self, maybe_options: Optional[dict] = None) -> None: ...
    
    def evaluate(self, key: str, ctx: dict, opts: Optional[dict] = None) -> EvaluateResponse: ...
    
    def async_evaluate(self,key: str, ctx: dict, opts: Optional[dict] = None) -> Awaitable[EvaluateResponse]: ...
    
    def create_decision(self, content: str) -> ZenDecision: ...
    
    def get_decision(self, key: str) -> ZenDecision: ...

class ZenDecision:
    def evaluate(self,ctx: dict, opts: Optional[dict] = None) -> EvaluateResponse: ...
    
    def async_evaluate(self,ctx: dict, opts: Optional[dict] = None) -> Awaitable[EvaluateResponse]: ...
    
    def validate(self) -> None: ...
    
def evaluate_expression(expression: str, ctx: Optional[dict] = None) -> Any: ...

def evaluate_unary_expression(expression: str, ctx: dict) -> bool: ...

def render_template(template: str, ctx: dict) -> Any: ...