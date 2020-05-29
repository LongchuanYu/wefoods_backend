import uuid
from datetime import datetime


print(uuid.uuid3(uuid.NAMESPACE_DNS,'liyang'+str(datetime.now())))