from translate import translate

def test_preserve_acronyms():
    src = "AWS IAM manages identities."
    out = translate(src, "fr")
    assert "AWS" in out and "IAM" in out

if __name__ == "__main__":
    test_preserve_acronyms()
    print("OK")
