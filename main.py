#!/usr/bin/env python
from constructs import Construct
from cdktf import App, NamedRemoteWorkspace, TerraformStack, TerraformOutput, RemoteBackend
from cdktf_cdktf_provider_aws import AwsProvider
from cdktf import Fn
from imports.aws import (
    s3
)


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)
        
        AwsProvider(self, "AWS", region="us-east-1")

        BUCKET_NAME = 'cdktf-python-demo-us-east-1'

        s3_lifecycle_rule = [
            { "enabled": True, "id": "abort-multipart", "prefix": "/", "abortIncompleteMultipartUploadDays": 7 },
            { "enabled": True, "transition": [{ "days": 30, "storageClass": "STANDARD_IA" }] },
            { "enabled": True, "noncurrentVersionTransition": [{ "days": 30, "storageClass": "STANDARD_IA" }] },
            { "enabled": False, "transition": [{ "days": 90, "storageClass": "ONEZONE_IA" }] },
            { "enabled": False, "noncurrentVersionTransition": [{ "days": 90, "storageClass": "ONEZONE_IA" }] },
            { "enabled": False, "transition": [{ "days": 365, "storageClass": "GLACIER" }] },
            { "enabled": False, "noncurrentVersionTransition": [{ "days": 365, "storageClass": "ONEZONE_IA" }] },
        ]
        s3_tags= {
            "Team": "Devops",
            "Company": "Your compnay"
        }
        s3_policy = {
            "Version": "2012-10-17",
            "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                "s3:GetObject"
                ],
                "Resource": [
                f"arn:aws:s3:::${BUCKET_NAME}/*"
                ]
            }
            ]
        }

        bucket = s3.S3Bucket(self,
            id=f"s3-{BUCKET_NAME}",
            bucket=f"s3-{BUCKET_NAME}",
            lifecycle_rule=s3_lifecycle_rule,
            tags=s3_tags,
            policy=str(s3_policy)
            )
        

        TerraformOutput(self, 'S3 id',value=bucket.id)
        TerraformOutput(self, 'S3 arn', value=bucket.arn)
        ################


app = App()
stack = MyStack(app, "aws")
app.synth()
