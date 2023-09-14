# ClassParser_v4 (4th version of ClassParser)
## Change
### Fixed
1. In ClassFuncParser.GetMemberTree method.
   Instead of listing all members of the specified class which are defined at top (for convenience, we call it as top-level class of the module.) .
   It can list all members of specified class (including nested class).

   I have tried <b>top-level class</b> and <b>nested class</b> which is defined as a child in class, ensuring that they are NO bugs.
   
    
### Added
