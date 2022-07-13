# lai_dbt_component component

This ⚡ [Lightning component](lightning.ai) ⚡ was generated automatically with:

```bash
lightning init component lai_dbt
```

## To run lai_dbt_component

First, install lai_dbt_component (warning: this app has not been officially approved on the lightning gallery):

```bash
lightning install component https://github.com/theUser/lai_dbt_component
```

Once the app is installed, use it in an app:

```python
from lai_dbt import TemplateComponent
import lightning_app as la


class LitApp(lapp.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.lai_dbt_component = TemplateComponent()

    def run(self):
        print(
            "this is a simple Lightning app to verify your component is working as expected"
        )
        self.lai_dbt_component.run()


app = lapp.LightningApp(LitApp())
```
