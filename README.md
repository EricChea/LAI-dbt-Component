> **Warning**
>
> #### THIS REPO IS EXPERIMENTAL

<!---:lai-name: dbt--->

<div align="center">
<img src="static/dbt.png" width="200px">

```
A Lightning component to run dbt as a lightning app component.
______________________________________________________________________
```

![Tests](https://github.com/PyTorchLightning/LAI-dbt-Component/actions/workflows/ci-testing.yml/badge.svg)

</div>

### About

This component lets you run dbt.

### Use the component

To run dbt

```python
import lightning as L
from lightning.app.storage import Path

from lai_dbt import DBT


class YourComponent(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.dbt_project_dir = Path("<PATH TO DBT PROJECT DIR>")
        self.dbt_profile_dir = Path("<PATH TO DBT PROFILE DIR>")
        self.dbt = DBT(self.dbt_project_dir)

    def run(self):
        self.dbt.execute_command(
            command=[
                "dbt",
                "run",
                "--project-dir",
                self.dbt_project_dir,
                "--profiles-dir",
                self.dbt_profile_dir,
            ],
        )


app = L.LightningApp(YourComponent())
```

### Install

Run the following to install:

```shell
git clone https://github.com/PyTorchLightning/LAI-dbt-Component
cd LAI-dbt-Component
pip install -r requirements.txt
pip install -e .
```

### Tests

To run unit tests locally:

```shell
# From the root level of the package (LAI-bigquery)
pip install -r tests/requirements.txt
pytest
```
