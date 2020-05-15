import procspec

yaml_path = './specs/very_complex_processor.yaml'
proc = procspec.parse_proc(yaml_path=yaml_path, default_output='src_field')
import pdb; pdb.set_trace()
