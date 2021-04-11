# -*- encoding: utf-8 -*_
import argparse
import bcrypt
from pprint import pprint as pp
import typing as T


def hash(passwd: T.Text) -> T.Dict[T.Text, T.Text]:
    bin_pass = passwd.encode("utf-8")
    bin_salt = bcrypt.gensalt(10)
    bin_hash = bcrypt.hashpw(bin_pass, bin_salt)
    return {"salt": bin_salt.decode("utf-8"), "hash": bin_hash.decode("utf-8")}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("plaintext", help="plaintext password to be hashed")
    args = parser.parse_args()

    pp(hash(args.plaintext))


if __name__ == "__main__":
    main()
