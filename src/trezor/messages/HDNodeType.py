# Automatically generated by pb2py
from protobuf import protobuf as p
t = p.MessageType()
t.add_field(1, 'depth', p.UVarintType, flags=p.FLAG_REQUIRED)
t.add_field(2, 'fingerprint', p.UVarintType, flags=p.FLAG_REQUIRED)
t.add_field(3, 'child_num', p.UVarintType, flags=p.FLAG_REQUIRED)
t.add_field(4, 'chain_code', p.BytesType, flags=p.FLAG_REQUIRED)
t.add_field(5, 'private_key', p.BytesType)
t.add_field(6, 'public_key', p.BytesType)
HDNodeType = t