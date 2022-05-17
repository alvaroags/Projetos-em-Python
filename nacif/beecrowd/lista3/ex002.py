seg = int(input())
hora = seg//3600
min = seg%3600 // 60
seg = seg %3600 %60
print(f'{hora}:{min}:{seg}')