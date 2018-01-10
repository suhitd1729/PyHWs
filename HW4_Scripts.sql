--HW 4 SQL 
--What is the average crime rate in each year? (Query)
select count(*)/2700000 AS 'Average Crime Rate' , Year from crime_details group by Year;

--Subset the list of crimes that occured at SIDEWALK and an arrest has been made. (Query, algebraic expression and expression tree)
select cd.* from crime_details cd , crime_incidents ci where cd.Crime_ID = ci.Crime_ID and cd.Location_Description = "SIDEWALK" and ci.Arrest = "TRUE";
select cd.* from crime_details cd INNER JOIN crime_incidents ci  ON cd.Crime_ID = ci.Crime_ID and cd.Location_Description = "SIDEWALK" and ci.Arrest = "TRUE";

--In the resulting dataset, identify the crime type that resulted in most crimes per each district. (Query)

select a.District, ct.Primary_Type as 'Most Crimes in the District'
from 
(select ci.District as 'District' ,cd.Primary_Type_ID  as 'Primary_Type_ID' , count(*) as 'Count' from crime_incidents ci , crime_details cd  where 
ci.Crime_ID = cd.Crime_ID and 
ci.Case_Number = cd.Case_Number  group by cd.Primary_Type_ID order by ci.District) a , 
crime_types ct
where a.Count = (select max(Count) from 
(select ci.District as 'District' ,cd.Primary_Type_ID  as 'Primary_Type_ID' , count(*) as 'Count' from crime_incidents ci , crime_details cd  where 
ci.Crime_ID = cd.Crime_ID and 
ci.Case_Number = cd.Case_Number  group by cd.Primary_Type_ID order by ci.District)  
as f where f.District = a.District) and 
a.Primary_Type_ID = ct.Primary_Type_ID order by a.District;

--List the crimes with FBI code = 26 and domestic? (Query, algebraic expression and expression tree)
select * from crime_incidents ci where ci.FBI_Code = 26 and ci.Domestic = "TRUE"; 

select cd.* from crime_incidents ci , crime_details cd where 
ci.FBI_Code = 26 
and ci.Domestic = "TRUE" 
and ci.Crime_ID = cd.Crime_ID
and ci.Case_Number = cd.Case_Number;


--What is the increase in the number of crimes involving thefts (primary crime type) from 2016 to 2017? (Query)
select count(*)-(select count(*) from crime_details cd , crime_types ct where cd.Primary_Type_ID = ct.Primary_Type_ID
and ct.Primary_Type ="THEFT" and cd.Year = 2016) as 'Increase in Thefts in 2017 over 2016' from crime_details cd , crime_types ct where cd.Primary_Type_ID = ct.Primary_Type_ID
and ct.Primary_Type ="THEFT" and cd.Year = 2017;

--What are the 3 most common types of crimes in 001XX N PARKSIDE AVE? Provide the corresponding crime counts for these crime types. (Query)
select ct.Primary_Type, count(*) as 'Count' from crime_details cd , crime_types ct where cd.block = '001XX N PARKSIDE AVE' and cd.Primary_Type_ID = ct.Primary_Type_ID group by cd.Primary_Type_ID order by Count Desc limit 3;


--Average days between the crime indcident date and last updated date. (Query)
SELECT avg(datediff(cd.Updated_On,ci.Date)) as 'Average diff between incident date and Last Updated date'  FROM
    crime_details cd,
    crime_incidents ci
WHERE
    cd.Crime_ID = ci.Crime_ID
	AND cd.Case_Number = ci.Case_Number;


--List the crimes that were committed on 4/30/2016 and updated on the same day. (Query, algebraic expression, expression tree)
select cd.* ,ci.date from crime_details cd , crime_incidents ci where 
cd.Crime_ID = ci.Crime_ID and 
cd.Case_Number = ci.Case_Number and
DATE(cd.Updated_On) = DATE(ci.date) and
DATE(ci.date) = str_to_date('4/30/2016','%e/%m/%Y' );


--Subset the list of crimes in 2016 that were domestic and occured on a STREET and an arrest was made. (Query, algebraic expression, expression tree)
SELECT cd.* FROM
    crime_details cd,
    crime_incidents ci
WHERE
    cd.Crime_ID = ci.Crime_ID
		AND cd.Case_Number = ci.Case_Number 
        AND cd.Location_Description = 'STREET'
        AND ci.Arrest = 'TRUE'
        AND ci.Domestic = 'TRUE'
        AND cd.Year = 2016;
		
--Are there any crimes that involved Telephone threats that occured in Disctric 10 and FBI code 30? (Query, algebraic expression, expression tree)
select cd.*,ci.FBI_Code,ci.District from crime_details cd, crime_incidents ci where cd.Crime_ID = ci.Crime_ID and 
cd.Case_Number = ci.Case_Number and ci.FBI_Code = 30 and ci.District = 10 and cd.Description = "TELEPHONE THREAT";