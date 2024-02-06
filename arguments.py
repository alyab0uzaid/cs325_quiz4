import argparse

def main():
    parser = argparse.ArgumentParser(description="Argument parsing example")
    parser.add_argument('string_arg', type=str, help='Input string')
    parser.add_argument('int_arg', type=int, help='Input integer')
    parser.add_argument('float_arg', type=float, help='Input float')

    args = parser.parse_args()
    print(f"String: {args.string_arg}, Integer: {args.int_arg}, Float: {args.float_arg}")

if __name__ == "__main__":
    main()
