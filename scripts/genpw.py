# -*- encoding: utf-8 -*_
import argparse
import bcrypt
import typing as T


def hash(passwd: T.Text) -> T.Text:
    bin_pass = passwd.encode("utf-8")
    bin_hash = bcrypt.hashpw(bin_pass, bcrypt.gensalt(10))
    return bin_hash.decode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("plaintext", help="plaintext password to be hashed")
    args = parser.parse_args()

    print(hash(args.plaintext))


if __name__ == "__main__":
    main()
