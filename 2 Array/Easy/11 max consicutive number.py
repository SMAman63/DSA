
def main(arr):
    maxcount=0
    count=0
    for i in arr:
        if i==1:
            count+=1
            print("count",count)
            if maxcount<count:
                maxcount=count
            continue
        print("maxcount",maxcount)
        print("count",count)
        if maxcount<count:
            maxcount=count
        count=0
    print(maxcount)


if __name__=="__main__":
    arr = [1,0,1,1,1,0,1,1,1,1,1]
    main(arr)
