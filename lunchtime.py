def is_lunchtime(X):
    return 1 <= X <= 4

# Main function to read inputs and call the helper function for each test case
def main():
    # Read the number of test cases
    T = int(input().strip())

    # Process each test case
    for _ in range(T):
        X = int(input().strip())
        if is_lunchtime(X):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
