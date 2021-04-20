import json

from procspec.proc_base import ProcessorBase
from procspec.parse import register_proc


@register_proc("Patchwise")
class PatchwiseProcessor(ProcessorBase):
    def __init__(self, **kwargs):
        self.args = kwargs

    def __call__(self, **kwargs):
        pass


import modelhouse
@register_proc("ApplyModel")
class ApplyModelProcessor(ProcessorBase):
    def __init__(self, path, **kwargs):
        self.model = modelhouse.load_model(path, params=json.dumps(kwargs))

    def __call__(self, args):
        return self.model(**args)

    def to(self, device):
        self.model = self.model.to(device)

