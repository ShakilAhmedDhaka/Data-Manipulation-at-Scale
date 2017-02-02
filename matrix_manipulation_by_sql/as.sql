/*SELECT count(*) FROM (
select term from frequency as fr where fr.docid="10398_txt_earn" and count=1)
;
*/
/*SELECT count(*) FROM (
select term from frequency as fr where fr.docid="10398_txt_earn" and count=1 
union  
select term from frequency as fr where fr.docid="925_txt_trade" and count=1)
;*/
/*SELECT count(*) FROM (
select distinct docid from frequency as fr where fr.term="law" or fr.term="legal")
;*/
/*select count(*) from (select count(term) as cnt from (select distinct term,docid from frequency) group by docid) 
where cnt>300;*/
/*select count(*) from (select distinct docid from frequency where term="transactions" intersect select distinct 
docid from frequency where term="world");*/
/*select a.row_num,b.col_num,sum(a.value*b.value) from a,b where a.col_num=b.row_num group by 
a.row_num,b.col_num;*/
/*select a.docid,b.docid,a.term,b.term,sum(a.count*b.count) from Frequency as a,Frequency as b where 
a.docid='10080_txt_crude' and b.docid='17035_txt_earn' and a.term=b.term group by a.docid,b.docid;*/


/*create view var as
SELECT * FROM frequency 
UNION
 SELECT 'q' as docid, 'washington' 
as term, 1 as count UNION 
SELECT 'q' as docid, 'taxes' as term, 1 as count 
UNION 

SELECT 'q' as docid, 'treasury' as term, 1 as count;*/
/*select max(ab) from (select sum(a.count*b.count) as ab from var as a,var as b where 
a.docid != 'q' and b.docid='q' and a.term=b.term group by a.docid,b.docid);*/