# Kode pundet på https://www.geeksforgeeks.org/python-program-for-merge-sort/
import timeit

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# Laver en midligtidligt array
	L = [0] * (n1)
	R = [0] * (n2)

	# Kopier data til vores arrays
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merger vores subarrays indtil vores sorterede array 
	i = 0	 # Start indeks af første subarray
	j = 0	 # Start indeks af anden subarray
	k = l	 # Start indeks af vores blandede array

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Kopier de resternde elementer fra vores vesntre subarray
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Kopier de resternde elementer fra vores højre subarray
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# l er for venstre indeks og r er for højre indeks 
# For vores subarrays i vores array der skal sorteres


def mergeSort(arr, l, r):
	if l < r:

		m = l+(r-l)//2

		# Sorter først og anden halvdel
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


# Kode til at køre implantationen
arr = [999, 998, 997, 996, 996, 994, 993, 993, 992, 990, 989, 988, 988, 988, 986, 986, 983, 983, 981, 980, 979, 979, 978, 975, 974, 973, 972, 971, 967, 967, 966, 964, 964, 962, 961, 960, 959, 957, 957, 955, 954, 954, 954, 953, 952, 951, 949, 948, 948, 948, 947, 946, 946, 943, 943, 941, 941, 941, 940, 940, 939, 937, 937, 935, 935, 934, 933, 932, 930, 929, 929, 929, 926, 926, 926, 926, 925, 923, 922, 922, 920, 920, 920, 920, 918, 918, 916, 915, 915, 914, 912, 912, 910, 910, 909, 908, 907, 904, 904, 904, 904, 904, 901, 897, 896, 895, 894, 893, 893, 892, 891, 891, 890, 890, 890, 889, 885, 885, 885, 882, 878, 878, 878, 878, 875, 873, 873, 
872, 872, 872, 869, 869, 868, 868, 868, 866, 866, 861, 860, 859, 859, 858, 857, 856, 856, 856, 854, 854, 852, 852, 851, 851, 851, 851, 850, 849, 849, 849, 847, 845, 845, 845, 845, 844, 843, 843, 841, 840, 838, 838, 837, 837, 837, 837, 834, 833, 832, 832, 831, 831, 831, 831, 831, 830, 830, 824, 824, 823, 823, 823, 822, 821, 820, 819, 818, 818, 817, 815, 813, 812, 812, 810, 810, 809, 809, 808, 808, 808, 807, 804, 803, 800, 800, 799, 798, 798, 794, 793, 790, 786, 786, 786, 786, 785, 784, 784, 783, 781, 781, 779, 779, 778, 777, 777, 776, 776, 775, 775, 775, 773, 771, 770, 769, 767, 767, 765, 764, 762, 761, 761, 760, 760, 758, 754, 753, 753, 751, 751, 749, 749, 749, 748, 747, 746, 746, 746, 744, 743, 739, 738, 733, 732, 730, 729, 728, 726, 724, 724, 724, 723, 720, 720, 719, 718, 718, 718, 
717, 717, 715, 715, 714, 713, 711, 710, 710, 709, 707, 706, 705, 705, 704, 702, 702, 702, 702, 700, 696, 696, 696, 696, 696, 694, 693, 692, 691, 691, 690, 686, 686, 684, 683, 683, 683, 682, 681, 681, 681, 680, 680, 678, 678, 674, 670, 669, 668, 668, 666, 666, 666, 663, 660, 659, 659, 658, 657, 657, 656, 656, 653, 653, 653, 651, 649, 649, 646, 646, 645, 644, 643, 639, 639, 639, 638, 637, 631, 631, 628, 628, 626, 625, 623, 622, 616, 616, 614, 614, 613, 613, 613, 612, 612, 611, 609, 608, 608, 607, 606, 604, 604, 602, 602, 600, 600, 600, 598, 597, 593, 592, 591, 591, 590, 590, 590, 589, 589, 589, 587, 587, 585, 583, 582, 581, 581, 581, 580, 579, 578, 577, 577, 576, 576, 573, 571, 571, 570, 569, 568, 566, 565, 565, 565, 564, 561, 559, 557, 556, 555, 554, 554, 554, 550, 549, 548, 547, 547, 
545, 545, 545, 544, 544, 543, 539, 537, 534, 533, 533, 533, 532, 531, 529, 528, 527, 526, 524, 524, 524, 524, 522, 521, 521, 520, 517, 517, 517, 512, 511, 511, 511, 511, 511, 509, 509, 508, 508, 508, 508, 507, 506, 506, 504, 504, 503, 503, 502, 502, 501, 500, 499, 499, 498, 496, 495, 494, 494, 492, 491, 490, 490, 490, 489, 489, 489, 488, 488, 485, 485, 483, 482, 482, 481, 479, 479, 479, 478, 477, 476, 474, 474, 474, 474, 472, 472, 472, 470, 470, 467, 466, 465, 463, 463, 462, 462, 462, 458, 457, 457, 457, 456, 455, 454, 454, 452, 451, 451, 451, 449, 447, 447, 446, 445, 444, 443, 443, 443, 442, 442, 442, 440, 439, 439, 436, 435, 434, 433, 432, 430, 430, 428, 427, 426, 424, 424, 423, 421, 421, 419, 417, 417, 415, 412, 412, 410, 408, 408, 407, 406, 405, 405, 404, 403, 401, 401, 400, 395, 
395, 395, 394, 394, 393, 392, 390, 388, 387, 387, 384, 382, 381, 380, 379, 375, 374, 373, 371, 370, 370, 369, 367, 366, 365, 361, 360, 358, 358, 358, 358, 357, 356, 356, 356, 356, 355, 355, 355, 353, 353, 347, 347, 346, 344, 344, 343, 343, 342, 340, 337, 336, 335, 334, 333, 332, 331, 329, 329, 326, 326, 326, 325, 324, 324, 322, 321, 318, 318, 318, 315, 314, 314, 314, 314, 313, 313, 311, 310, 307, 307, 306, 306, 305, 304, 303, 303, 302, 300, 296, 293, 293, 290, 290, 289, 289, 289, 286, 285, 283, 281, 281, 281, 279, 278, 278, 278, 277, 277, 276, 275, 274, 273, 271, 271, 271, 271, 269, 266, 265, 265, 262, 261, 261, 260, 259, 259, 258, 257, 256, 255, 255, 254, 253, 253, 252, 252, 251, 251, 248, 247, 246, 246, 245, 241, 240, 239, 239, 238, 238, 238, 237, 236, 236, 231, 230, 229, 226, 226, 
225, 225, 224, 222, 221, 219, 218, 218, 217, 217, 216, 216, 216, 215, 212, 212, 212, 211, 210, 208, 207, 207, 206, 205, 205, 204, 204, 203, 202, 202, 199, 198, 198, 197, 196, 195, 193, 193, 192, 190, 190, 189, 187, 183, 181, 180, 178, 177, 175, 174, 173, 172, 172, 170, 169, 167, 167, 166, 165, 163, 162, 162, 162, 162, 162, 161, 161, 160, 160, 160, 160, 156, 153, 150, 150, 149, 148, 146, 144, 142, 141, 136, 136, 133, 133, 133, 132, 130, 128, 127, 126, 126, 125, 124, 124, 123, 123, 121, 121, 118, 118, 117, 116, 114, 114, 112, 111, 110, 110, 109, 108, 108, 107, 107, 105, 102, 102, 99, 99, 98, 98, 97, 96, 96, 94, 90, 90, 88, 88, 88, 87, 87, 86, 84, 83, 83, 82, 81, 81, 79, 79, 78, 78, 78, 77, 76, 76, 76, 73, 69, 68, 68, 66, 66, 66, 65, 65, 64, 63, 63, 61, 60, 59, 59, 57, 57, 57, 57, 57, 57, 56, 56, 55, 55, 55, 51, 50, 50, 50, 50, 50, 49, 48, 44, 43, 42, 41, 40, 37, 36, 36, 35, 35, 34, 33, 32, 31, 31, 29, 29, 29, 27, 26, 25, 25, 25, 24, 23, 22, 22, 20, 20, 19, 18, 17, 16, 15, 13, 13, 13, 10, 10, 9, 8, 8, 8, 7, 6, 6, 6, 5, 5, 5, 4, 3, 1, 0]
n = len(arr)
print("Given array is")
for i in range(n):
	print("%d" % arr[i]),

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % arr[i]),
print(timeit.timeit())

# Koden er skrevet af Mohit Kumra.
# Her har jeg selv adder en lille del til at tælle hvor hurtigt koden køre.
print(timeit.timeit())
