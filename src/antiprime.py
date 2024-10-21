def main(x) :
    ## YOU CODE SHOULD START HERE AST THE SAME
    ## IDENTATION AS THIS COMMENT
    c = 1
    z = 0

    while c <= x :
        if (x % c == 0) :
            z = z+1
        c = c+1

    x = x-1
    y = 0
    while x >= 1 and y < z :
        c = 1
        y = 0
        while c <= x :
            if (x % c == 0) :
                y = y+1
            c = c+1
        x = x-1

    if y >= z :
        return("not anti-prime")
    else :
        return("anti-prime")


## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
    import sys
    x = int(sys.argv[1])
    print(main(x))

