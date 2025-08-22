from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_iam
    # aws_sqs as sqs,
)
from constructs import Construct

class SabalShresthaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "SabalShresthaQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        lambda_function = _lambda.Function(
            self, "SabalShresthaFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            # handler="HelloWorld.lambda_handler",
            handler="WebHealthLambda.lambda_handler",
            code=_lambda.Code.from_asset("./modules"),
            timeout=Duration.seconds(20)
        )
        # Add permission to publish metrics to CloudWatch
        lambda_function.add_to_role_policy(
            aws_iam.PolicyStatement(
                effect=aws_iam.Effect.ALLOW,
                actions=["cloudwatch:PutMetricData"],
                resources=["*"]
            )
        )