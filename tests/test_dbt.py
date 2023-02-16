r"""To test a lightning component:

1. Init the component.
2. call .run()
"""
from lai_dbt.component import DBT


def test_placeholder_component():
    messenger = DBT()
    messenger.run()
