bessie_first_line = input()
bessie_second_line = input()

elsie_first_line = input()
elsie_second_line = input()


if len(bessie_first_line) == 0 or len(bessie_second_line) == 0:
    print("NO")
elif len(elsie_first_line) == 0 or len(elsie_second_line) == 0:
    print("NO")
else:
    # vertical case



    bessie_element_set = set()
    # horizontal first line
    bessie_element_set.add(bessie_first_line[0] + bessie_first_line[1])
    # vertical second column
    bessie_element_set.add(bessie_first_line[1] + bessie_second_line[1])
    # horizontal second line
    bessie_element_set.add(bessie_second_line[1] + bessie_second_line[0])
    # vertical first column
    bessie_element_set.add(bessie_second_line[0] + bessie_first_line[0])

    elsie_element_set = set()
    # horizontal first line
    elsie_element_set.add(elsie_first_line[0] + elsie_first_line[1])
    # vertical second column
    elsie_element_set.add(elsie_first_line[1] + elsie_second_line[1])
    # horizontal second line
    elsie_element_set.add(elsie_second_line[1] + elsie_second_line[0])
    # vertical first column
    elsie_element_set.add(elsie_second_line[0] + elsie_first_line[0])

    best_friends = False
    for bessie_element in bessie_element_set:
        if "X" in bessie_element: continue
        if bessie_element in elsie_element_set:
            best_friends = True
            break
    if best_friends:
        print("YES")
    else:
        print("NO")