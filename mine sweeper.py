import random

def arr_out(arr,arr_output,arr_result,n,flg):         #for displaying output
    res_to_out(arr_result,arr_output,n)
    color(arr_output,n)
    print('')
    print('\033[1;33;20m Bombs :',n,"   Flags :",flg)
    print('')
    print(end=("     "))
    for x in range(1,n-1):
        print("\033[1;36;20mY" + str(x),end = ("  "))
    print('\n')
    a = 1
    for row in arr_output:
        print("\033[1;35;20m  X"+str(a),end=('  '))
        a += 1
        print("   ".join(str(cell) for cell in row))
        print('')
    return arr_output

def res_to_out(arr_result,arr_output,n):
    for i in range(n-2):
        for j in range(n-2):
            arr_output[i][j] = arr_result[i+1][j+1]
            if arr_output[i][j] == 0:
                arr_output[i][j] = '\033[1;37;20m.\033[1;37;20m'
            if arr_output[i][j] == '-':
                arr_output[i][j] = '\033[1;37;40m-\033[0;37;20m' 
    return (arr_result,arr_output)

def remove_flag(arr,arr_output,arr_result,n,flg,count):
    x = input("\033[1;32;20mEnter matrix value to remove flag/'exit' to exit\n\n    X :  ")
    if x.lower() == 'exit':
        print("\n\033[1;33;20mReturning to defusing BOMBS")
        main_game(arr,arr_output,arr_result,n,flg,count)
    if x.isdigit() != True:
        print("\n\033[1;31;20mEntered value of X is invalid please type again")
        flag(arr,arr_output,arr_result,n,flg,count)
    y = input("\033[1;32;20m    Y :  ")
    if y.lower() == 'exit':
        print("\n\033[1;33;20mReturning to defusing BOMBS")
        main_game(arr,arr_output,arr_result,n,flg,count)
    if y.isdigit() != True:
        print("\n\033[1;31;20mEntered value of Y is invalid please type again")
        flag(arr,arr_output,arr_result,n,flg,count)
    if int(x) > n or int(y) > n:
        print("\n\033[1;31;20mEntered value of X or Y is invalid please type again")
        flag(arr,arr_output,arr_result,n,flg,count)
    x = int(x) - 1
    y = int(y) - 1
    if arr_result[x+1][y+1] != 'F' or flg == n:
        print("\033[1;31;20mThere is no flag to remove at this point")
        main_game(arr,arr_output,arr_result,n,flg,count)
    arr_result[x+1][y+1] = '-'
    flg += 1
    arr_out(arr,arr_output,arr_result,n,flg)
    return main_game(arr,arr_output,arr_result,n,flg,count)

def flag(arr,arr_output,arr_result,n,flg,count):
    x = input("\033[1;32;20mEnter matrix value to place flag/'exit' to exit\n\n    X :  ")
    if x.lower() == 'exit':
        print("\n\033[1;33;20mReturning to defusing BOMBS")
        main_game(arr,arr_output,arr_result,n,flg,count)
    if x.isdigit() != True:
        print("\n\033[1;31;20mEntered value of X is invalid please type again")
        flag(arr,arr_output,arr_result,n,flg,count)
    y = input("\033[1;32;20m    Y :  ")
    if y.lower() == 'exit':
        print("\n\033[1;33;20mReturning to defusing BOMBS")
        main_game(arr,arr_output,arr_result,n,flg,count)
    if y.isdigit() != True:
        print("\n\033[1;31;20mEntered value of Y is invalid please type again")
        flag(arr,arr_output,arr_result,n,flg,count)
    if int(x) > n or int(y) > n:
        print("\n\033[1;31;20mEntered value of X or Y is invalid please type again")
        flag(arr,arr_output,arr_result,n,flg,count)
    x = int(x) - 1
    y = int(y) - 1
    if arr_result[x+1][y+1] != '-' or flg == 0:
        print("\033[1;31;20mYou can't place flag there")
        main_game(arr,arr_output,arr_result,n,flg,count)
    arr_result[x+1][y+1] = "F"
    flg -= 1
    arr_out(arr,arr_output,arr_result,n,flg)
    return main_game(arr,arr_output,arr_result,n,flg,count)

def count_dash(arr_result,n,count2):
    for i in range(1,n-1):
        for j in range(1,n-1):
            if arr_result[i][j] == "-" or arr_result[i][j] == "F" and arr[i][j] == "X":
                count2 += 1 
    if count2 == n:
        flg = 0
        game_over(arr_output,arr_result,arr,n,count,count2,flg)
    else:
        return count2

def game_over(arr_output,arr_result,arr,n,count,count2,flg):
    print("\033[1;31;20m\n**************************************************\n")
    print("                  GAME OVER\n")
    print("**************************************************")
    defused_bombs = 0
    for_score = (n*n) - count
    for i in range(1,n-1):
        for j in range(1,n-1):
            if arr[i][j] == "X" and arr_result[i][j] != 'F' :
                arr_result[i][j] = arr[i][j]
            if arr_result[i][j] == "F" and arr[i][j] == "X":
                arr_result[i][j] = 'F'
                defused_bombs += 1
            if arr_result[i][j] == "F" and arr[i][j] != "X":
                arr_result[i][j] = ('\033[1;37;41m'+str(arr[i][j])+'\033[1;37;40m\033[0;37;20m')
    if count2 == n:
        defused_bombs = n
        for i in range(1,n-1):
            for j in range(1,n-1):
                if arr[i][j] == "X":
                    arr_result[i][j] = 'F'
    arr_out(arr,arr_output,arr_result,n,flg)
    score = (for_score * defused_bombs)
    print("\n\033[1;32;20m**************************************************\n")
    print("           SCORE :",score,"  BOMB DEFUSED :",defused_bombs,'\n')
    print("**************************************************\n")
    print("\033[1;32;20m**************************************************\n")
    print("\033[1;32;20m               Thanks for playing\n")
    print("**************************************************")
    input()
    exit()
            
def defusing(arr_result,arr,n):
    count1 = 50
    while count1 > 0:
        for x in range(1,n-1):
            for y in range(1,n-1):
                if arr_result[x][y] == 0 :
                    if arr_result[x][y-1] != 'F':
                        arr_result[x][y-1] = arr[x][y-1]
                    if arr_result[x][y+1] != 'F':
                        arr_result[x][y+1] = arr[x][y+1]
                    if arr_result[x-1][y] != 'F':
                        arr_result[x-1][y] = arr[x-1][y]
                    if arr_result[x+1][y] != 'F':
                        arr_result[x+1][y] = arr[x+1][y]
        count1 -= 1
    return arr_result

def color(arr_output,n):
    for i in range(n-2):
        for j in range(n-2):
            if arr_output[i][j] == "X":
                arr_output[i][j] = "\033[1;31;20mX\033[1;36;20m"
            if arr_output[i][j] == "F":
                arr_output[i][j] = "\033[1;37;42mF\033[1;37;40m\033[0;37;20m"
            if arr_output[i][j] == 1 or arr_output[i][j] == '1':
                arr_output[i][j] = "\033[1;30;20m1\033[1;36;20m"
            if arr_output[i][j] == 2 or arr_output[i][j] == '2':
                arr_output[i][j] = "\033[1;32;20m2\033[1;36;20m"
            if arr_output[i][j] == 3 or arr_output[i][j] == '3':
                arr_output[i][j] = "\033[1;33;20m3\033[1;36;20m"
            if arr_output[i][j] == 4 or arr_output[i][j] == '4':
                arr_output[i][j] = "\033[1;34;20m4\033[1;36;20m"
            if arr_output[i][j] == 5 or arr_output[i][j] == '5':
                arr_output[i][j] = "\033[1;35;20m5\033[1;36;20m"
            if arr_output[i][j] == 6 or arr_output[i][j] == '6':
                arr_output[i][j] = "\033[1;36;20m6\033[1;36;20m"
            if arr_output[i][j] == 7 or arr_output[i][j] == '7':
                arr_output[i][j] = "\033[1;37;20m7\033[1;36;20m"
            if arr_output[i][j] == 8 or arr_output[i][j] == '8':
                arr_output[i][j] = "\033[1;38;20m8\033[1;36;20m"
    return arr_output

def hint(arr,n):
    for i in range(1,n-1):
        for j in range(1,n-1):
            if arr[i][j] != "X":
                if arr[i-1][j-1] == "X":
                    arr[i][j] += 1
                if arr[i-1][j]   == "X":
                    arr[i][j] += 1
                if arr[i-1][j+1] == "X":
                    arr[i][j] += 1
                if arr[i][j-1]   == "X":
                    arr[i][j] += 1
                if arr[i][j+1]   == "X":
                    arr[i][j] += 1
                if arr[i+1][j-1] == "X":
                    arr[i][j] += 1
                if arr[i+1][j]   == "X":
                    arr[i][j] += 1
                if arr[i+1][j+1] == "X":
                    arr[i][j] += 1
    return arr
    
def plant(num_bomb,arr,n):
    if num_bomb == 0:
        return arr
    else:
        i = random.randrange(1,n-1,1)
        j = random.randrange(1,n-1,1)
        if arr[i][j] != "X":
            arr[i][j] = "X"
            num_bomb -= 1
        return plant(num_bomb,arr,n)

def main_game(arr,arr_output,arr_result,n,flg,count):
    count2 = 0
    x = input("\033[1;32;20mEnter matrix value to defuse/type 'exit' to exit game\n\n    X :  ")
    if x.lower() == "exit":
        game_over(arr_output,arr_result,arr,n,count,count2,flg)
    if x.lower() == "flag":
        flag(arr,arr_output,arr_result,n,flg,count)
        main_game(arr,arr_output,arr_result,n,flg,count)
    if x.lower() == "remove flag":
        remove_flag(arr,arr_output,arr_result,n,flg,count)
        main_game(arr,arr_output,arr_result,n,flg,count)
    if x.isdigit() != True:
        print("\n\033[1;31;20mEntered value of X is invalid please type again\n")
        main_game(arr,arr_output,arr_result,n,flg,count)
    y = input("\033[1;32;20m    Y :  ")
    if x.lower() == "exit":
        game_over(arr_output,arr_result,arr,n,count,count2,flg)
    if y.lower() == "flag":
        flag(arr,arr_output,arr_result,n,flg,count)
        main_game(arr,arr_output,arr_result,n,flg,count)
    if y.lower() == "remove flag":
        remove_flag(arr,arr_output,arr_result,n,flg,count)
        main_game(arr,arr_output,arr_result,n,flg,count)
    if y.isdigit() != True:
        print("\n\033[1;31;20mEntered value of Y is invalid please type again\n")
        main_game(arr,arr_output,arr_result,n,flg,count)
    x = int(x) - 1
    y = int(y) - 1
    if x > n or y > n:
        print("\n\033[1;31;20mEntered values are invalid")
        main_game(arr,arr_output,arr_result,n,flg,count)
    arr_result[x+1][y+1] = arr[x+1][y+1]
    count_dash(arr_result,n,count2)
    if arr_result[x+1][y+1] == "X":
        game_over(arr_output,arr_result,arr,n,count,count2,flg)
    count += 1
    defusing(arr_result,arr,n)
    arr_out(arr,arr_output,arr_result,n,flg)
    main_game(arr,arr_output,arr_result,n,flg,count)
    
n = int(input("\033[1;32;20mEnter the length of mine as per difficulty : ")) #length of matrix
num_bomb = n + 2   #int(input("enter the no. of bombs : "))
flg = num_bomb          #lives
count = 0
n += 2
arr = [[0 for i in range(n)] for j in range(n)]
arr_result = [['-' for i in range(n)] for j in range(n)]
arr_output = [['-' for i in range(n-2)] for j in range(n-2)]
plant(int(num_bomb),arr,n)
hint(arr,n)
print("\n**************************************************************************")
print("         \n*** game instructions ***\n")
print("1. Enter matrix value of X & Y to defuse in mine")
print("2. Enter string 'flag' at place of entering X")
print("   then enter X & Y values to place flag")
print("3. Enter string 'remove flag' at place of entering X")
print("   then enter X & Y values to remove flag")
print("4. To exit game type 'exit'\n")
print("**************************************************************************")

arr_out(arr,arr_output,arr_result,n,flg)
main_game(arr,arr_output,arr_result,n,flg,count)