def merge(file1, file2, out):
    with open(file1, 'r') as input_file1:
        with open(file2, 'r') as input_file2:
            with open(out, 'w') as output:
                for s1, s2 in zip(input_file1, input_file2):
                    s1 = s1.split()
                    s2 = s2.split()
                    if s1 == s2:
                        output.writelines(f"{' '.join(s1 and s2)}\n")
                    else:
                        output.writelines(f"{'>>>file1>>>'}\n")
                        output.writelines(f"{' '.join(s1)}\n")
                        output.writelines(f"{'===='}\n")
                        output.writelines(f"{' '.join(s2)}\n")
                        output.writelines(f"{'<<<file2<<<'}\n")


print(merge('./INPUT_OUT/text1.txt',
            './INPUT_OUT/text2.txt', './INPUT_OUT/out_merge.txt'))
print(open('./INPUT_OUT/out_merge.txt').read())
