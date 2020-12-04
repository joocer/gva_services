from gva.data.flows import BaseOperator
from .create_http_task import create_http_task


class GoogleTaskOperator(BaseOperator):

    def execute(self, data={}, context={}):

        google_task_queue = context.get("google_task_queue", "reply")

        create_http_task(
            project="vulnerability-analytics",
            queue=google_task_queue,
            url='',
            payload=context)