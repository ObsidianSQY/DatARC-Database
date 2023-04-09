# coding: utf-8

# Import portion


import pandas as pd
import numpy as np


# Read file and parse data from researchers tab
# Fill value -1 when there exsists blank
# filename: Name of file to use


def readTableResearch(filename):
    try:
        xl = pd.ExcelFile(filename)
        df1 = xl.parse('Researchers')
        df1.fillna("NULL", inplace=True)
    except Exception:
        df1 = pd.read_csv(filename)
        df1.fillna("NULL", inplace=True)
    return df1


def getVTARCrank(dataframe, value):
    return dataframe.loc[dataframe[' Rank (VT-ARC)'] == value]


# Get value info with range from table in specific column
# E.g. format: In column "Rank", the value range is: left(1) <= Result < right(5)
# E.g. Parameter: (dataframe, "Rank", "<=", "<", 1, 5)
# dataframe: data of table
# condition1: condition set for left filter
# condition2: condition set for right filter
# left: left value of condition
# right: right value of condition


def rangeFilter(dataframe, columnName, condition1, condition2, left, right):
    if (left > right):
        if (condition1 == ">" and condition2 == ">"):
            return dataframe.loc[(dataframe[columnName] > right) & (dataframe[columnName] < left)]
        elif (condition1 == ">" and condition2 == ">="):
            return dataframe.loc[(dataframe[columnName] >= right) & (dataframe[columnName] < left)]
        elif (condition1 == ">=" and condition2 == ">"):
            return dataframe.loc[(dataframe[columnName] > right) & (dataframe[columnName] <= left)]
        elif (condition1 == ">=" and condition2 == ">="):
            return dataframe.loc[(dataframe[columnName] >= right) & (dataframe[columnName] <= left)]
        else:
            return "INVALID CONDITION"
    else:
        if (condition1 == "<" and condition2 == "<"):
            return dataframe.loc[(dataframe[columnName] < right) & (dataframe[columnName] > left)]
        elif (condition1 == "<" and condition2 == "<="):
            return dataframe.loc[(dataframe[columnName] <= right) & (dataframe[columnName] > left)]
        elif (condition1 == "<=" and condition2 == "<"):
            return dataframe.loc[(dataframe[columnName] < right) & (dataframe[columnName] >= left)]
        elif (condition1 == "<=" and condition2 == "<="):
            return dataframe.loc[(dataframe[columnName] <= right) & (dataframe[columnName] >= left)]
        else:
            return "INVALID CONDITION"
    


# Get rank value with range from table
# E.g. format: left(1) <= Result < right(5)
# E.g. Parameter: (dataframe, "<=", "<", 1, 5)
# dataframe: data of table
# condition1: condition set for left filter
# condition2: condition set for right filter
# left: left value of condition
# right: right value of condition


def getRankRange(dataframe, condition1, condition2, left, right):
    return rangeFilter(dataframe, ' Rank (VT-ARC)', condition1, condition2, left, right)


# Get source value from table
# dataframe: data of table
# source_type: specific string required


def getVTARCsource(dataframe, source_type):
    return dataframe.loc[dataframe['Source'] == source_type]


# Get first name value from table
# dataframe: data of table
# string: specific string required


def getVTARCfirstName(dataframe, string):
    return dataframe.loc[dataframe['Name'] == string]


# Get last name value from table
# dataframe: data of table
# string: specific string required


def getVTARClastName(dataframe, string):
    return dataframe.loc[dataframe['Last Name'] == string]


# Get institution name value from table
# dataframe: data of table
# string: specific string required


def getVTARCinstitution(dataframe, string):
    return dataframe.loc[dataframe['Institution'] == string]


# Get title value from table
# dataframe: data of table
# string: specific string required


def getVTARCtitle(dataframe, string):
    return dataframe.loc[dataframe['Title'] == string]


# Get domain value from table
# dataframe: data of table
# string: specific string required


def getVTARCdomain(dataframe, string):
    return dataframe.loc[dataframe['Domain'] == string]


# Get gender value from table
# dataframe: data of table
# string: specific string required


def getVTARCgender(dataframe, string):
    return dataframe.loc[dataframe['Gender'] == string]


# Get topic value from table
# dataframe: data of table
# string: specific string required


def getVTARCtopic(dataframe, string):
    return dataframe.loc[dataframe['Topic'] == string]


# Get description value from table
# dataframe: data of table
# string: specific string required


def getVTARCdescription(dataframe, string):
    return dataframe.loc[dataframe['Research Description'] == string]


# Get field value from table
# dataframe: data of table
# string: specific string required


def getVTARCfield(dataframe, string):
    return dataframe.loc[dataframe['Research Fields'] == string]


# Get other key value from table
# dataframe: data of table
# key: specific key required


def getVTARCotherKey(dataframe, key):
    return dataframe.loc[dataframe['Other Key notes'] == key]


# Get relevant link value from table
# dataframe: data of table
# link: specific string required


def getVTARCrelevantLinks(dataframe, link):
    return dataframe.loc[dataframe['Relevant links'] == link]


# Get email value from table
# dataframe: data of table
# email: specific string required


def getVTARCemail(dataframe, email):
    return dataframe.loc[dataframe['email'] == email]


# Get first name value from table
# dataframe: data of table
# site: specific site required


def getVTARCwebsite(dataframe, site):
    return dataframe.loc[dataframe['Website'] == site]


# Get first name value from table
# dataframe: data of table
# num: specific value required


def getVTARCpubCount(dataframe, num):
    return dataframe.loc[dataframe['Pub Count'] == num]


# Get pub count value with range from table
# dataframe: data of table
# condition: condition set for filter
# left: left value of condition
# right: right value of condition


def getPubCountRange(dataframe, condition1, condition2, left, right):
    if (left == right):
        return getVTARCpubCount(dataframe, left)
    return rangeFilter(dataframe, 'Pub Count', condition1, condition2, left, right)


# Get cite count value from table
# dataframe: data of table
# num: specific num required


def getVTARCciteCount(dataframe, num):
    return dataframe.loc[dataframe['Citation count'] == num]


# Get cite count value with range from table
# dataframe: data of table
# condition: condition set for filter
# left: left value of condition
# right: right value of condition


def getCiteCountRange(dataframe, condition1, condition2, left, right):
    if (left == right):
        return getVTARCciteCount(dataframe, left)
    return rangeFilter(dataframe, 'Citation count', condition1, condition2, left, right)


# Get H-index value from table
# dataframe: data of table
# index: specific index required


def getVTARChindex(dataframe, index):
    return dataframe.loc[dataframe['H-Index'] == index]


# Get index range value with range from table
# dataframe: data of table
# condition: condition set for filter
# left: left value of condition
# right: right value of condition


def getIndexRange(dataframe, condition1, condition2, left, right):
    if (left == right):
        return getVTARChindex(dataframe, left)
    return rangeFilter(dataframe, 'H-Index', condition1, condition2, left, right)


# Get H5-index value from table
# dataframe: data of table
# index: specific index required


def getVTARCh5index(dataframe, index):
    return dataframe.loc[dataframe['H5-Index (5year)'] == index]


# Get H5 index value with range from table
# dataframe: data of table
# condition: condition set for filter
# left: left value of condition
# right: right value of condition


def getH5Range(dataframe, condition1, condition2, left, right):
    if (left == right):
        return getVTARCh5index(dataframe, left)
    return rangeFilter(dataframe, 'H5-Index (5year)', condition1, condition2, left, right)


# Get id value from table
# dataframe: data of table
# num: specific id number required


def getVTARCid(dataframe, num):
    return dataframe.loc[dataframe['ID'] == num]


# Add limitation to column
# dataframe: data of table
# columnName: according to which coloumn
# key: specific keyword to filter


def limitation(dataframe, columnName, keyword):
    return dataframe.loc[dataframe[columnName] == keyword]

