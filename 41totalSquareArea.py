# 正方形の合計面積
# 1辺1の正方形をスタートとして、1辺の長さ、正方形の個数を列ごとに増加させていきます。
# i列の中には1辺iの正方形がi個あり、i列に含まれる正方形の合計面積を計測します。
# 自然数xが与えられるので、1列からx列までに含まれる全ての正方形の面積の合計値を返す
# totalSquareAreaという関数を再帰によって作成してください。
# 総和や3乗を計算するために必要な他の関数は用いて構いません。


def totalSquareArea(x):
    #ここから書きましょう
    theSquareArea = x * (x * x)
    if x <= 0:
        return 0
    return theSquareArea +  totalSquareArea(x-1)