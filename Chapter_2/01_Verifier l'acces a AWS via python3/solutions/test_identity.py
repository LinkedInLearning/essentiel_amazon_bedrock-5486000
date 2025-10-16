import boto3

def main():
    sts = boto3.client("sts")
    ident = sts.get_caller_identity()
    print("Account:", ident.get("Account"))
    print("UserId:", ident.get("UserId"))
    print("Arn:", ident.get("Arn"))

if __name__ == "__main__":
    main()
