## This will prepare the data for the Redshift database. 
    1) Goes to the directory where all the files are stored
        a. Searches through all the files that contain fs220
        b. Append the endings of these files to a list [fs220A, fs220B, fs220C, etc...]
        c. Get the unique endings from that list by taking the set()
        d. Now we have all the unique endings (we will make a seperate table in our Redshift Database for each)
        
    2) For each ending, we find the most recent year and month of the reported data 
       This is needed to get the latest_vars variable
        a. First it finds most recent year reported for that ending (for loop with > comparisons)
        b. Then it finds most recent month reported in that year for that ending (for loop with > comparisons)
        c. It appends each year and month combination for each ending to lists
          (*NOTE: this is necessary as there is not a universal latest year and month for each ending. 
          For example, fs220E does not report in 201706, but instead, its last reporting is in 201606)
          
    3) Using the zip() function, we can iterate over three lists at a time (ending list, latest year list, latest month list) 
         a. We get the latest vars for that ending
         b. We then run through the main loop with that ending and complete the steps as before:
            i.    Reads in all fs220(ending) files 
            ii.   Makes all the column names uppercase
            iii.  Compares columns names to columns names of the latest variables using list comprehension
            iv.   If df is missing latest columns, includes them and fills with NaN, this is to maintain order - COPY into 
                  Redshift
            v.    Adds an ORDERS column which is a sequential index
            vi.   Adds a unique identifier with CU_NUM_DATE 
            vii.  Adds two columns, QUARTER, and YEAR, in case we may use these to query later on
            viii. Final structure is all df's(all years, months, and endings) with all the latest columns in a dictionary 
                  The df's are all standardized
                  If latest column doesn't exist in the original df, it is filled with NaN's. 
                  (*NOTE: we made need to change what it is filled in with here since NaN is a float and we really want   
                  NULL/None for Redshift Database to read correctly)
    
    4) Write all the dictionary files to a new folder to load into AWS S3 bucket 
       Add naming convention of same prefix for each file.
       Example: fs220A-csv. is prefix for all fs220A files (all years and months)
