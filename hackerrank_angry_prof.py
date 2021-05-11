def angryProfessor(k, a):

    th_count=0
    for i in range(len(a)):
        if (a[i]<=0):
            th_count+=1
    if (th_count>=k):
        return "NO"
    return "YES"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        first_multiple_input = raw_input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = map(int, raw_input().rstrip().split())

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
