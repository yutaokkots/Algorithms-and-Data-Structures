'''
433. Minimum Genetic Mutation
Medium

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene 
where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. 
A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, 
return the minimum number of mutations needed to mutate from startGene to endGene. 
If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

        "AACCGGTT" <- startGene
         |||||||X
        "AACCGGTA" <- endGene

        "bank": ["AACCGGTA"]

Example 2:
Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

        "AACCGGTT" <- startGene
         |||||||X
        "AACCGGTA"          
         ||X|||||
        "AAACGGTA" <- endGene

        ["AACCGGTA","AACCGCTA","AAACGGTA"] 

Constraints:
    0 <= bank.length <= 10
    startGene.length == endGene.length == bank[i].length == 8
    startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
'''
from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        bank_set = set(bank)
        nucleotides = ["A", "T", "C", "G"]
        queue = deque()
        queue.append(startGene)

        visited = set()
        visited.add(startGene)

        count = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                gene = queue.popleft()
                if gene == endGene:
                    return count
                for j in range(8):
                    for na in nucleotides:
                        new_gene = gene[:j] + na + gene[j+1:]
                        if (new_gene in bank_set and 
                                new_gene not in visited):
                            visited.add(new_gene)
                            queue.append(new_gene)
            count += 1
        return -1
                    

        '''
            AAT [0, 1, 0]
            AAA
            TAA
        
            ['AAA' ,'TAT', 'TAA', 'GGA']
        '''