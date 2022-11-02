# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(s, sub):
    return [s[z:z+len(sub)] for z in range(len(s))].count(sub)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)