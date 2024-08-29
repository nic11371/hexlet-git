def make_diff_view(diff1, diff2, fout):
    fout.writelines(f"{'>>>file1>>>'}\n")
    fout.writelines(f"{''.join(diff1)}=====\n")
    fout.writelines(f"{''.join(diff2)}")
    fout.writelines(f"{'<<<file2<<<'}\n")


def merge(file1, file2, out):
    diff1 = []
    diff2 = []
    with open(file1) as input1, open(file2) as input2, open(out, 'w') as fout:
        for s1, s2 in zip(input1, input2):
            if s1 == s2:
                if diff1 or diff2:
                    make_diff_view(diff1, diff2, fout)
                    diff1 = []
                    diff2 = []
                fout.writelines(f"{''.join(s1)}")
            diff1.append(s1)
            diff2.append(s2)
            # fout.writelines(make_diff_view(diff1, diff2))
    # return diff1, diff2
            # else:
            #     fout.writelines(f"{'>>>file1>>>'}\n")
            #     fout.writelines(f"{' '.join(s1)}\n")
            #     fout.writelines(f"{'===='}\n")
            #     fout.writelines(f"{' '.join(s2)}\n")
            #     fout.writelines(f"{'<<<file2<<<'}\n")


print(merge('./INPUT_OUT/text1.txt',
            './INPUT_OUT/text2.txt', './INPUT_OUT/out_merge.txt'))
print(open('./INPUT_OUT/out_merge.txt').read())
