def finddigits(s):

    # Strings of digits 0-9
    num = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    # Initialize vector
    arr = [0] * (10)

    # Initialize answer
    ans = ""

    # Size of the string
    n = len(s)

    # Traverse the string
    for i in range(n):
        if s[i] == "z":
            arr[0] += 1
        if s[i] == "w":
            arr[2] += 1
        if s[i] == "g":
            arr[8] += 1
        if s[i] == "x":
            arr[6] += 1
        if s[i] == "v":
            arr[5] += 1
        if s[i] == "o":
            arr[1] += 1
        if s[i] == "s":
            arr[7] += 1
        # if s[i] == "f":
        #     arr[4] += 1
        if s[i] == "u":
            arr[4] += 1
        if s[i] == "h":
            arr[3] += 1
        if s[i] == "i":
            arr[9] += 1

    # Update the elements of the vector
    arr[7] -= arr[6]
    arr[5] -= arr[7]
    # arr[4] -= arr[5]
    arr[1] -= arr[2] + arr[4] + arr[0]
    arr[3] -= arr[8]
    arr[9] -= arr[5] + arr[6] + arr[8]

    # Print the digits into their
    # original format
    for i in range(10):
        for j in range(arr[i]):
            ans += chr((i) + ord("0"))

    # Return answer
    return ans


# Driver Code
if __name__ == "__main__":

    s1 = "owoftnuoer"
    s2 = "zesxrionezoreo"

    print(finddigits(s1))
    print(finddigits(s2))
