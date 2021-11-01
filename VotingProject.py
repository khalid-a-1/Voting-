#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 08:37:05 2018

Claire Larsen, Amna khalid, Malaika Charrington
Nov 26, 2018
VotingProject.py

Group project that go through different types of voting and creates programs 
for these different voting systems
"""
import string
#==============================================================================
def Read(filename):
    '''
    This function reads the file in and creates a list of lists for the 
    individual ballots
    
    Input: 
        filename: text file
    Return:
        list of lists
    '''
    file = open(filename, 'r')
    Voting = []
    for line in file:
        Ballot = line.split()
        Voting.append(Ballot)
    file.close()
    return Voting

#==============================================================================
    
def Candidates(BigList):
    '''
    This function creates a list of just the candidtes on the ballot 
    Input: 
        BigList: list of lists that gives the information from the ballots
    Return: 
        list of candidates
    '''
    CandidateList = []
    for Ballot in BigList:
        for i in range(len(Ballot)):
            if Ballot[i] not in CandidateList:
                CandidateList.append(Ballot[i])
    return CandidateList

#==============================================================================    
def printing(results):
    '''
    This function prints the results in a table format 
    Input: 
        results: a dictionary of the final counts
    Return: 
        Prints the results in a Key: value format 
    '''
    for key in results: 
        print (str(key) + ":" + str(results[key]))
        
#==============================================================================
        
def Plurality (BigList, CandidateList):
    '''
    This function calculates the purality voting system or the number of first
    ranks each candidate recieved
    
    Input: 
        BigList: list of lists that gives the information from the ballots
        CandidateList: 
    Return: 
        d = dictionary 
    '''
    d = {}
    for c in CandidateList:
        d[c] = 0
    for Ballot in BigList:
        if Ballot[0] in CandidateList:
            d[Ballot[0]] = d[Ballot[0]]+1
    return d

#==============================================================================
    
def Majority(dictionary, BigList):
    '''
    This function finds if there is a majority winner in a race
    Input: 
        dictionary: dictionary of the results from plurality
        BigList: list of lists that gives the information from the ballots
    Return: 
        A candidate if there is a winner or none if no one won majority
    '''
    for key in dictionary:
        if dictionary[key]/(len(BigList)) >= .5:
            return key
        else:
            return 'none'

#==============================================================================
            
def borda(BigList):
    '''
    This function finds the score for candidates using the borda method
    Input: 
        BigList:List of lists that has the ballots and the approvals
    Return: 
        d = dictionary of the candidates and their scores
    '''
    d = {}
    for c in BigList[0]:
        d[c] = 0
    n = len(BigList[0])
    for ballot in BigList:
        for k in range(0,n):
            d[ballot[k]] = d[ballot[k]] + (n - k)
           
    return d

#==============================================================================
    
def Approval(BigList, CandidateList):
    '''
    This function finds the counts for candidates using the approval method
    Input: 
        BigList: List of lists that has the ballots and the approvals 
        CandidateList: List of the candidates
    Return: 
        d = dictionary of the candidates and their scores
    '''
    d = {}
    for c in CandidateList:
        d[c] = 0
    for Ballot in BigList:
        for i in range(len(Ballot)):
            if Ballot[i] in 'ABCDE':
                d[Ballot[i]] = d[Ballot[i]]+1
    return d

#==============================================================================
def isWinner(data, c1,c2):
    '''
    This function finds the winner of a head to head voting process
    Input: 
        data: List of lists that has the ballots and the approvals 
        c1: candidate 1
        c2: candidate 2
    Return: 
        True if c1 wins False if c2 wins
    '''
    c1score = 0
    c2score = 0
    for ballot in data:
        if ballot.index(c1)<ballot.index(c2):
             c1score = c1score + 1
        else: 
            c2score = c2score +1
    if c1score > c2score:
        return True
    else: 
        return False

#==============================================================================      
def condorcet (CandidateList, BigList):
    '''
    This function finds the winner of the condorcet voting system 
    Input: 
        BigList: List of lists that has the ballots and the approvals 
        CandidateList: List of the candidates
    Return:
        Candidate that wins or there is no winner if no candidate wins
    '''
    for c1 in CandidateList:
        c = 0
        for c2 in CandidateList:
            if c1 != c2: 
                pairs = (c1, c2)
                if (isWinner(BigList, pairs[0], pairs[1])) == True :
                    c = c + 1
                else: 
                    c = c + 0         
        if c == len(CandidateList)-1: 
            return pairs[0]
        else:
            return ('There is no winner')

#==============================================================================
    
def main():
    
    #Reading in files 
    filename = 'data.txt'
    filename2 = 'approval.txt'
    
    Voting = Read(filename)
    ApprovalList = Read(filename2)
    
    CandidateList1 = Candidates(Voting)
    CandidateList2 = Candidates(ApprovalList)
    
    #Plurality
    Method1 = Plurality(Voting, CandidateList1)
    print('Plurality Resutls:')
    printing(Method1)
    print('\n')
    
    #Majority
    Method2 = Majority(Method1, Voting)
    print('Majority Results:')
    print(Method2, '\n')
    
    #Borda
    Method3 = borda(Voting)
    print('Borda Results:')
    printing(Method3)
    print('\n')
    
    #Approval
    Method4 = Approval(ApprovalList, CandidateList2)
    print('Approval Results:')
    printing(Method4)
    print('\n')
    
    #Condorcet
    Method5 = condorcet(CandidateList1, Voting)
    print('Condorcet')
    print(Method5)
    

main()