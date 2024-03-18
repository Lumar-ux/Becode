# def sort_sequence(sequence):
#     sorted_sequence = []
#     sm=0
#     for i in range(0, len(sequence), 3):
#         filter_slice = list(filter(lambda x: x!=0, sequence))
#         slice_of_three = filter_slice[i:i+3]
#         sorted_slice = sorted(slice_of_three)
#         sorted_sequence.append(sorted_slice) 
#     sorted_array = sorted(sorted_sequence, key=lambda  x: sum(x))
#     flat_list = sum(sorted_array, [])
#     for i in range(0, len(flat_list)+3, 4):
#         flat_list.insert(i+3, 0)
#     return(flat_list)
# # print(sort_sequence([3,2,1,0,5,6,4,0,1,5,3,0,4,2,8,0]))
# # # output [1,2,3,0,1,3,5,0,2,4,8,0,4,5,6,0]

# print(sort_sequence([3,2,1,0,5,6,4,0,1,5,3,0,2,2,2,0]))
# # output [2,2,2,0,1,2,3,0,1,3,5,0,4,5,6,0]
# # print(sort_sequence([2,2,2,0,5,6,4,0,1,5,3,0,3,2,1,0]))
# # # output [2,2,2,0,1,2,3,0,1,3,5,0,4,5,6,0]


def sort_sequence(sequence):
    sub_sequences_3 = []
    start = 0
    for i, num in enumerate(sequence):
        if (num == 0):
            sub_sequences_3.append(sequence[start:i+1])
            start = i + 1
    sorted_sequence = []
    for i in sub_sequences_3:
        sort_filter_0 = sorted(filter(lambda x: x!=0, i))
        sorted_sequence.append(sort_filter_0) 
    sorted_sequence.sort(key=lambda sub_sequences_3: sum(sub_sequences_3))
    result = []
    for i in sorted_sequence:
        result.extend(i)
        result.append(0)
    return(result)
# print(sort_sequence([3,2,1,0,5,6,4,0,1,5,3,0,4,2,8,0]))
# # output [1,2,3,0,1,3,5,0,2,4,8,0,4,5,6,0]

print(sort_sequence([3,2,1,0,5,6,4,0,1,5,3,0,2,2,2,0]))
# output [2,2,2,0,1,2,3,0,1,3,5,0,4,5,6,0]
# print(sort_sequence([2,2,2,0,5,6,4,0,1,5,3,0,3,2,1,0]))
# # output [2,2,2,0,1,2,3,0,1,3,5,0,4,5,6,0]