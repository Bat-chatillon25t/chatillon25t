__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from .create_custom_attribute import CreateCustomAttribute as CreateCustomAttribute
from .create_custom_attribute_entry import CreateCustomAttributeEntry as CreateCustomAttributeEntry
from .create_test_resource import CreateTestResource as CreateTestResource
from .create_test_resource_machine import CreateTestResourceMachine as CreateTestResourceMachine
from .delete_custom_attribute import DeleteCustomAttribute as DeleteCustomAttribute
from .delete_test_resource import DeleteTestResource as DeleteTestResource
from .retrieve_custom_attributes import RetrieveCustomAttributes as RetrieveCustomAttributes
from .retrieve_latest_custom_attribute_entry import RetrieveLatestCustomAttributeEntry as RetrieveLatestCustomAttributeEntry
from .retrieve_test_resource import RetrieveTestResource as RetrieveTestResource
from .retrieve_test_resource_ids import RetrieveTestResourceIds as RetrieveTestResourceIds
from .retrieve_test_resource_machine import RetrieveTestResourceMachine as RetrieveTestResourceMachine
from .retrieve_test_resource_machine_by_resource_location_id import RetrieveTestResourceMachineByResourceLocationId as RetrieveTestResourceMachineByResourceLocationId
from .start_delete_test_resource_machine import StartDeleteTestResourceMachine as StartDeleteTestResourceMachine
from .update_custom_attribute import UpdateCustomAttribute as UpdateCustomAttribute