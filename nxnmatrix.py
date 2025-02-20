r = input()
print("no of cols")
c = input()
mat = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(mat[i][j])
    mat.append(row)
trans=[]
for i in range(r):
    row = []
    for j in range(c):
        row.append(mat[i][j])
    mat.append(row)
if mat==trans:
    print("symmetric")
else:
    print("not")