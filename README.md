# Documentation

* Explore the Terraform for Terraform [CLI](https://www.terraform.io/downloads.html) >= v1.0+
* Explore the CDK for cdktf [CLI](https://github.com/hashicorp/terraform-cdk#build)

Add your AWS credentials as two environment variables, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY, replacing AAAAAA with each respective values.

```shell
export AWS_ACCESS_KEY_ID=AAAAAA
export AWS_SECRET_ACCESS_KEY=AAAAA
```

## cdktf-python-aws-s3bucket

AWS s3 bucket configuration with python and cdktf

### Usage

Install project dependencies

```shell
cdktf get
```

Generate CDK for Terraform constructs for Terraform provides and modules used in the project.

```bash
cdktf synth
```
