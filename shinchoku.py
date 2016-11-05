"""
進捗バーを表示する。
進捗どうですか？
"""
import sys

def shinchoku(list_obj, size=20):
    for index, element in enumerate(list_obj):
        # list_objの計測
        list_len = len(list_obj)
        ratio = (index+1) / list_len

        # 進捗バーの描画
        drow_len = int(ratio * size)    # 完了した部分の長さ
        undrow_len = size - drow_len    # 未完の部分の長さ
        bar = "[" + "#"*drow_len + " "*undrow_len + "]"
        sys.stdout.write("{} {:.1%}\r".format(bar, ratio))
        sys.stdout.flush()

        yield element
