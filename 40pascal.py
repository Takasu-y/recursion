# パスカルの三角形
# 図のように三角数の数列があります。
# 天才Pascalは小学生の時にこの並びを見て規則的な発見をしました。
# 整数xが与えられるので、x番目の三角形に含まれるドットの数を返す、
# numberOfDotsという関数を再帰を使って作成してください。

def numberOfDots(x):
    #ここから書きましょう
    if x <= 1:
        return 1
    return x + numberOfDots(x-1)

print(numberOfDots(5))