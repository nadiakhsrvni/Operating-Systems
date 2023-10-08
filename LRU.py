size = int(input())
ram_capacity = int(input())
page_capacity = int(input())
page_size = int(ram_capacity / page_capacity)
process_list = []


#while(True):
#    try:
#        inp = input()
#        process_list.append(int(inp))
#    except EOFError as e:
#        break


print(f'page size: {page_size}')


while(True):
    inp = input()
    if not inp:
        break
    process_list.append(int(inp))


for i in range(len(process_list)):
    process_list[i] = int((process_list[i]/page_capacity))+1
    print(process_list[i])


pages = []
page_faults = 0


for i in process_list:
    if i not in pages:
        if len(pages) == page_size:
            pages.remove(pages[0])
            pages.append(i)

        else:
            pages.append(i)
        page_faults += 1

    else:
        pages.remove(i)
        pages.append(i)

print(page_faults)