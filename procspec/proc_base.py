import six


class ProcessorList(list):
    def __init__(self, *kargs, **kwargs):
        super().__init__(*kargs, **kwargs)


class ProcessorDict(dict):
    def __init__(self, *kargs, **kwargs):
        super().__init__(*kargs, **kwargs)


class ProcessorBase:
    def recursive_apply(self, func_name, func_args=[], func_kwargs={}):
        if hasattr(v, func_name):
            getattr(v, func_name)(*func_args, **func_kwargs)

        for name, v in var(self):
            if isinstance(v, ProcessorBase):
                v.recursive_apply(func_name, func_args, func_kwargs)
            elif isinstance(v, ProcessorList):
                for sv in v:
                    sv.recursive_apply(func_name, func_args, func_kwargs)

            elif isinstance(v, ProcessorDict):
                for _, sv in six.iteritems(v):
                    sv.recursive_apply(func_name, func_args, func_kwargs)


class Processor(ProcessorBase):
    def __init__(self):
        self.input_keys = None
        self.output_key = None
        self.procs = ProcessorList()

    def __call__(self, args, output_key=None):
        if self.input_keys is not None:
            input_args = {k: args[v] for k, v in self.input_keys.items()}
        else:
            input_args = args
        for proc in self.procs:
            # each proc is modifying the input args
            v = proc(input_args)

        if output_key is None:
            output_key = self.output_key
        if output_key is not None:
            args[output_key] = v

        return v
