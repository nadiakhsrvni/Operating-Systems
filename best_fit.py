ram_size = int(input())
ram = [ram_size]
allocation = ['Free']
array = []
need_compression = True
compress_count = 0

while(True):
    try:
        inp = input()
        array.append(inp.split(' '))
    except EOFError as e:
        break

#while(True):
#    inp = input()
#    if not inp:
#        break
#    array.append(inp.split(' '))


def find_max(arr):
    max = 0
    index = -1
    for i in range(len(arr)):
        if arr[i] >= max:
            max = arr[i]
            index = i
    return index


def compress(ram, allocation):
    free_count = 0
    for i in range(len(allocation)):
        if allocation[i] == 'Free':
            free_count += ram[i]
            ram[i] == -1

    for i in range(len(allocation)-1, -1, -1):
        if allocation[i] == 'Free':
            allocation.pop(i)
            ram.pop(i)
    if free_count > 0:
        ram.append(free_count)
        allocation.append('Free')


def best_fit():
    global need_compression, compress_count
    for i in range(len(array)):

        if array[i][0] == 'REQUEST':
            best_fit = find_max(ram)
            for j in range(len(ram)):

                if int(array[i][2]) <= ram[j] and ram[j] <= ram[best_fit] and allocation[j] == 'Free':
                    best_fit = j
                    need_compression = False

            if need_compression:
                compress_count += 1
                compress(ram, allocation)
                best_fit = find_max(ram)
                for j in range(len(ram)):
                    if int(array[i][2]) <= ram[j] and ram[j] <= ram[best_fit] and allocation[j] == 'Free':
                        best_fit = j

            allocation.insert(best_fit, array[i][1])
            ram.insert(best_fit, int(array[i][2]))
            ram[best_fit + 1] -= ram[best_fit]

            if ram[best_fit+1] == 0:
                ram.pop(best_fit+1)
                allocation.pop(best_fit + 1)

            need_compression = True

        else:  # RELEASE
            j = 0
            length = len(allocation);
            while length > 0 and j < len(allocation):
                if allocation[j] == array[i][1]:
                    allocation[j] = 'Free'
                    if j > 0:
                        if allocation[j - 1] == 'Free':
                            ram[j-1] = ram[j - 1] + ram[j]
                            allocation.pop(j)
                            ram.pop(j)
                            length -= 1
                            j -= 1
                j += 1


if __name__ == '__main__':
    best_fit()

    output = []
    for i in range(len(ram)):
        if allocation[i] == 'Free':
            output.append(ram[i])
        else:
            output.append(allocation[i])

    string_output = ''
    for el in output:
        string_output = string_output + str(el) + ' '
    string_output = string_output[:-1]

    print(compress_count)
    print(string_output)

    exit()