# def make_diff_view(diff1, diff2):
#     line1 = []
#     line2 = []
#     line1.append(diff1)
#     line2.append(diff2)
#     return line1, line2


def merge(file1, file2, out):
    str1 = []
    str2 = []
    with open(file1) as f1, open(file2) as f2, open(out, 'w') as fout:
        for diff1, diff2 in zip(f1, f2):
            if diff1 != diff2:
                str1.append(diff1)
                str2.append(diff2)
            fout.write(f"{"".join(str1)}")
            # if diff1 or diff2:
            #     fout.write(make_diff_view(diff1, diff2))
            

                    # if s1 == s2:
                    #     output.writelines(f"{' '.join(s1 and s2)}\n")
                    # else:
                    #     output.writelines(f"{'>>>file1>>>'}\n")
                    #     output.writelines(f"{' '.join(s1)}\n")
                    #     output.writelines(f"{'===='}\n")
                    #     output.writelines(f"{' '.join(s2)}\n")
                    #     output.writelines(f"{'<<<file2<<<'}\n")

#  if diff1 or diff2: 
    #  fout.write(make_diff_view(diff1, diff2)) diff1 = [] diff2 = []


print(merge('./INPUT_OUT/text1.txt',
            './INPUT_OUT/text2.txt', './INPUT_OUT/out_merge.txt'))
print(open('./INPUT_OUT/out_merge.txt').read())
