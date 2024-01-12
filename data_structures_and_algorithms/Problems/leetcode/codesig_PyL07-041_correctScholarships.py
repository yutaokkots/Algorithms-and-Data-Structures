'''
correct Scholarships

For the upcoming academic year the Coolcoders University should decide which students will get the scholarships. Scholarships are considered to be correctly distributed if all best students have it, but not all students in the university do. Obviously, only university students should be able to get a scholarship, i.e. there should be no outsiders in the list of the students that will get a scholarships.

You are given lists of unique student ids bestStudents, scholarships and allStudents, representing ids of the best students, students that will get a scholarship and all the students in the university, respectively. Return true if the scholarships are correctly distributed and false otherwise.

For bestStudents = [3, 5], scholarships = [3, 5, 7], and
allStudents = [1, 2, 3, 4, 5, 6, 7], the output should be
solution(bestStudents, scholarships, allStudents) = true;

'''

def solution(bestStudents, scholarships, allStudents):
    print(f"{set(bestStudents)=} <= {set(scholarships)=} < {set(allStudents)=}")
    return set(bestStudents) <= set(scholarships) < set(allStudents)

bestStudents = [3, 5]
scholarships = [3, 5, 7]
allStudents = [1, 2, 3, 4, 5, 6, 7]

ans = solution(bestStudents, scholarships, allStudents)
print(ans)

# set(bestStudents)={3, 5} <= set(scholarships)={3, 5, 7} < set(allStudents)={1, 2, 3, 4, 5, 6, 7}
# True



bestStudents = [3]
scholarships = [1, 3, 5]
allStudents = [1, 2, 3]

ans2 = solution(bestStudents, scholarships, allStudents)
print(ans2)

# set(bestStudents)={3} <= set(scholarships)={1, 3, 5} < set(allStudents)={1, 2, 3}
# False