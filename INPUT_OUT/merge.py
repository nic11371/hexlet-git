def make_diff_view(diff1, diff2):
    return f'''>>>file1>>>
{''.join(diff1)}=====
{''.join(diff2)}<<<file2<<<\n'''


def merge(file1, file2, out):
    diff1 = []
    diff2 = []
    with open(file1) as input1, open(file2) as input2, open(out, 'w') as fout:
        for str1, str2 in zip(input1, input2):
            if str1 == str2:
                if diff1 or diff2:
                    fout.write(make_diff_view(diff1, diff2))
                    diff1 = []
                    diff2 = []
                fout.write(str1)
            else:
                diff1.append(str1)
                diff2.append(str2)
        if diff1 or diff2:
            fout.write(make_diff_view(diff1, diff2))


print(merge('./INPUT_OUT/text1.txt',
            './INPUT_OUT/text2.txt', './INPUT_OUT/out_merge.txt'))
print(open('./INPUT_OUT/out_merge.txt').read())
