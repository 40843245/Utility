# NumberSplitter (2th version)
## Preface
To see the introduction of question. See the images in GitHub. 

https://github.com/40843245/Utility/tree/main/Number/Algorithm/NumberSplitter/v2

To see ideas what I came up with it and how it works. See the idea.odt which available in 

https://github.com/40843245/Utility/blob/main/Number/Algorithm/NumberSplitter/v2/idea.odt

### NOTICE
I had found unexpected output with code of version 1 ( in ../v1/ directory).

DO NOT use code of version 1. Update code to this version instead.

## Fixed
Find the answer. 

## Examples
### Example 1
#### Code
    MAX_NUMBER = 100
    
    handler = NumberSplitter()    
    handler.Build(MAX_NUMBER)
    
    for i in range(1,MAX_NUMBER,1):      
        r = handler.resultTable[i]
        print("The max product of elem whose sum of elem is equal to "+str(i)+" is " + str(r))
#### Output
    The max product of elem whose sum of elem is equal to 1 is 1
    The max product of elem whose sum of elem is equal to 2 is 1
    The max product of elem whose sum of elem is equal to 3 is 2
    The max product of elem whose sum of elem is equal to 4 is 4
    The max product of elem whose sum of elem is equal to 5 is 6
    The max product of elem whose sum of elem is equal to 6 is 9
    The max product of elem whose sum of elem is equal to 7 is 12
    The max product of elem whose sum of elem is equal to 8 is 18
    The max product of elem whose sum of elem is equal to 9 is 27
    The max product of elem whose sum of elem is equal to 10 is 36
    The max product of elem whose sum of elem is equal to 11 is 54
    The max product of elem whose sum of elem is equal to 12 is 81
    The max product of elem whose sum of elem is equal to 13 is 108
    The max product of elem whose sum of elem is equal to 14 is 162
    The max product of elem whose sum of elem is equal to 15 is 243
    The max product of elem whose sum of elem is equal to 16 is 324
    The max product of elem whose sum of elem is equal to 17 is 486
    The max product of elem whose sum of elem is equal to 18 is 729
    The max product of elem whose sum of elem is equal to 19 is 972
    The max product of elem whose sum of elem is equal to 20 is 1458
    The max product of elem whose sum of elem is equal to 21 is 2187
    The max product of elem whose sum of elem is equal to 22 is 2916
    The max product of elem whose sum of elem is equal to 23 is 4374
    The max product of elem whose sum of elem is equal to 24 is 6561
    The max product of elem whose sum of elem is equal to 25 is 8748
    The max product of elem whose sum of elem is equal to 26 is 13122
    The max product of elem whose sum of elem is equal to 27 is 19683
    The max product of elem whose sum of elem is equal to 28 is 26244
    The max product of elem whose sum of elem is equal to 29 is 39366
    The max product of elem whose sum of elem is equal to 30 is 59049
    The max product of elem whose sum of elem is equal to 31 is 78732
    The max product of elem whose sum of elem is equal to 32 is 118098
    The max product of elem whose sum of elem is equal to 33 is 177147
    The max product of elem whose sum of elem is equal to 34 is 236196
    The max product of elem whose sum of elem is equal to 35 is 354294
    The max product of elem whose sum of elem is equal to 36 is 531441
    The max product of elem whose sum of elem is equal to 37 is 708588
    The max product of elem whose sum of elem is equal to 38 is 1062882
    The max product of elem whose sum of elem is equal to 39 is 1594323
    The max product of elem whose sum of elem is equal to 40 is 2125764
    The max product of elem whose sum of elem is equal to 41 is 3188646
    The max product of elem whose sum of elem is equal to 42 is 4782969
    The max product of elem whose sum of elem is equal to 43 is 6377292
    The max product of elem whose sum of elem is equal to 44 is 9565938
    The max product of elem whose sum of elem is equal to 45 is 14348907
    The max product of elem whose sum of elem is equal to 46 is 19131876
    The max product of elem whose sum of elem is equal to 47 is 28697814
    The max product of elem whose sum of elem is equal to 48 is 43046721
    The max product of elem whose sum of elem is equal to 49 is 57395628
    The max product of elem whose sum of elem is equal to 50 is 86093442
    The max product of elem whose sum of elem is equal to 51 is 129140163
    The max product of elem whose sum of elem is equal to 52 is 172186884
    The max product of elem whose sum of elem is equal to 53 is 258280326
    The max product of elem whose sum of elem is equal to 54 is 387420489
    The max product of elem whose sum of elem is equal to 55 is 516560652
    The max product of elem whose sum of elem is equal to 56 is 774840978
    The max product of elem whose sum of elem is equal to 57 is 1162261467
    The max product of elem whose sum of elem is equal to 58 is 1549681956
    The max product of elem whose sum of elem is equal to 59 is 2324522934
    The max product of elem whose sum of elem is equal to 60 is 3486784401
    The max product of elem whose sum of elem is equal to 61 is 4649045868
    The max product of elem whose sum of elem is equal to 62 is 6973568802
    The max product of elem whose sum of elem is equal to 63 is 10460353203
    The max product of elem whose sum of elem is equal to 64 is 13947137604
    The max product of elem whose sum of elem is equal to 65 is 20920706406
    The max product of elem whose sum of elem is equal to 66 is 31381059609
    The max product of elem whose sum of elem is equal to 67 is 41841412812
    The max product of elem whose sum of elem is equal to 68 is 62762119218
    The max product of elem whose sum of elem is equal to 69 is 94143178827
    The max product of elem whose sum of elem is equal to 70 is 125524238436
    The max product of elem whose sum of elem is equal to 71 is 188286357654
    The max product of elem whose sum of elem is equal to 72 is 282429536481
    The max product of elem whose sum of elem is equal to 73 is 376572715308
    The max product of elem whose sum of elem is equal to 74 is 564859072962
    The max product of elem whose sum of elem is equal to 75 is 847288609443
    The max product of elem whose sum of elem is equal to 76 is 1129718145924
    The max product of elem whose sum of elem is equal to 77 is 1694577218886
    The max product of elem whose sum of elem is equal to 78 is 2541865828329
    The max product of elem whose sum of elem is equal to 79 is 3389154437772
    The max product of elem whose sum of elem is equal to 80 is 5083731656658
    The max product of elem whose sum of elem is equal to 81 is 7625597484987
    The max product of elem whose sum of elem is equal to 82 is 10167463313316
    The max product of elem whose sum of elem is equal to 83 is 15251194969974
    The max product of elem whose sum of elem is equal to 84 is 22876792454961
    The max product of elem whose sum of elem is equal to 85 is 30502389939948
    The max product of elem whose sum of elem is equal to 86 is 45753584909922
    The max product of elem whose sum of elem is equal to 87 is 68630377364883
    The max product of elem whose sum of elem is equal to 88 is 91507169819844
    The max product of elem whose sum of elem is equal to 89 is 137260754729766
    The max product of elem whose sum of elem is equal to 90 is 205891132094649
    The max product of elem whose sum of elem is equal to 91 is 274521509459532
    The max product of elem whose sum of elem is equal to 92 is 411782264189298
    The max product of elem whose sum of elem is equal to 93 is 617673396283947
    The max product of elem whose sum of elem is equal to 94 is 823564528378596
    The max product of elem whose sum of elem is equal to 95 is 1235346792567894
    The max product of elem whose sum of elem is equal to 96 is 1853020188851841
    The max product of elem whose sum of elem is equal to 97 is 2470693585135788
    The max product of elem whose sum of elem is equal to 98 is 3706040377703682
    The max product of elem whose sum of elem is equal to 99 is 5559060566555523
## API
### NOTICE
Notice that 

To get expected result. Build it first. Then access resultTable attr. 

DO NOT use dynamicTable attr. Otherwise, one may get unexpected result.

For more details, see below.

### class NumberSplitter()
#### def Build()

Build. Or exactly to say, update the dynamicTable and resultTable from 0 to max of 3 and number where n must be a positive integer.

Syntax :
        
    def Build(self,number:int)

Parameter :
1. number : A positive number that indicates a end index that will be updated to. (Updates from 0 to max of 3 and number, see above.)

Returned Value :
    
    None
    
#### def Clear()

Clear all contents of attrs (i.e. dynamicTable and resultTable).

Syntax :

    def Clear(self)
  
Parameter :

    None

Returned Value :

    None

## Appreciation

## Release Notes
### 2023/10/10 10:21
Initial Notes.
### 2023/10/10 12:00
Added some files.

    psuedoCode.txt
    idea.odt
