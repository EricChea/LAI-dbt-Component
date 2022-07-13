from lai_dbt import DBT
import os
import lightning as L
from lightning.app.storage import Path

class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.dbt_project_dir = Path("sample_dbt/sample_dbt")
        self.dbt_profile_dir = Path("sample_dbt/sample_dbt")
        self.gcp_credentials_file = Path(os.getenv("BIGQUERY_SERVICE_ACCOUNT_KEYPATH"))
        self.dbt = DBT(self.dbt_project_dir)
        if not self.gcp_credentials_file.is_file():
            with open(self.gcp_credentials_file, "w") as _file:
                _file.write(os.getenv("BIGQUERY_SERVICE_ACCOUNT_CREDENTIALS"))


    def run(self):
        # Load to Path
        if not self.gcp_credentials_file.is_file():
            return

        self.dbt.execute_command(
            command = [
                "dbt", "run", "--project-dir", self.dbt_project_dir,
                "--profiles-dir", self.dbt_profile_dir
            ],
        )

# Set credentials path
os.environ["BIGQUERY_SERVICE_ACCOUNT_KEYPATH"] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "bq_credentials"
)

app = L.LightningApp(LitApp())
