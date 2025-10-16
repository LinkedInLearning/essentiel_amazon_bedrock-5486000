import boto3

def main():
    sts = boto3.client("sts")
    # Verifier l'accès à AWS via python3
    print(" afficher l'id:", sts.get_caller_identity())
    
if __name__ == "__main__":
    main()

