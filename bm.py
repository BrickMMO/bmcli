#! /usr/bin/env python

import argparse

def test():
    return 'working'

def main():
    parser = argparse.ArgumentParser(description="Simple Calculator CLI")

    parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'], help="Operation to perform")
    parser.add_argument('x', type=float, help="First number")
    parser.add_argument('y', type=float, help="Second number")

    args = parser.parse_args()

    if args.operation == 'add':
        result = add(args.x, args.y)
    elif args.operation == 'subtract':
        result = subtract(args.x, args.y)
    elif args.operation == 'multiply':
        result = multiply(args.x, args.y)
    elif args.operation == 'divide':
        result = divide(args.x, args.y)

    print(f"Result: {result}")

if __name__ == '__main__':
    main()
