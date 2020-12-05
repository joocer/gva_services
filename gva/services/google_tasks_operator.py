from gva.data.flows import BaseOperator
from .create_http_task import create_http_task



class GoogleTaskOperator(BaseOperator):

    def __init__(self, credentials_file='creds.json'):
        super().__init__()
        from google.oauth2 import service_account
        self.credentials = service_account.Credentials.from_service_account_file(
            credentials_file, scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

    def execute(self, data={}, context={}):

        google_task_queue = context.get("google_task_queue", "reply")

        create_http_task(
            project="vulnerability-analytics",
            queue=google_task_queue,
            url='',
            payload=context,
            credentials=self.credentials)