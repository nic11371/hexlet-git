def make_diff_view(diff1, diff2):
    if diff1 == diff2:
        return f"{''.join(diff1)}\n", f"{''.join(diff2)}\n"
    return (f"{'>>>file1>>>'}\n{''.join(diff1)}{'====='}",
            f"\n{''.join(diff2)}{'<<<file2<<<'}\n")


def merge(file1, file2, out):
    diff1 = []
    diff2 = []
    with open(file1) as input1, open(file2) as input2, open(out, 'w') as fout:
        for s1, s2 in zip(input1, input2):
            if s1 == s2:
                if diff1 or diff2:
                    fout.writelines(make_diff_view(diff1, diff2))
                    diff1 = []
                    diff2 = []
                fout.writelines(f"{''.join(s2)}")
            else:
                diff1.append(s1 if '\n' in s1 else s1 + '\n')
                diff2.append(s2 if '\n' in s2 else (s2 + '\n'))
        fout.writelines(make_diff_view(diff1, diff2))


print(merge('./INPUT_OUT/text1.txt',
            './INPUT_OUT/text2.txt', './INPUT_OUT/out_merge.txt'))
print(open('./INPUT_OUT/out_merge.txt').read())
