#Given: A string s of length at most 200 letters and four integers a, b, c and d

#Return: The slice of this string from indices a through b and c through d (with
# space in between), inclusively. In other words, we should include elements 
#s[b] and s[d] in our slice.

string = 'SLuuPmW6ctsA5TGI8pM13yfcejgLcGSytNE3aoK6HKNTcgkrXaSUm1cLampropeltisHLagobio4Y7wgqYj71GhEsvlX8ddImEj1sZ0sfDANmgrFF0SdEJ68fg4eTVsTmfhOxXow0Zl09xPJLAxiZCY7jyTHNgXR6zqM2XnofLkJAxRCSy8UlpGQoXP'
a, b, c, d = 55, 66, 70, 74

slice_a_b = string[a:b+1]
slice_c_d = string[c:d+1]

print(slice_a_b)
print(slice_c_d)