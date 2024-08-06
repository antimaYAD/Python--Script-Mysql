use sales;
select * from store;

select products,quatity,revenu,
rank() over (partition by region order by revenu desc) as highest_revenu
from store;	

select products,quatity,revenu,
dense_rank() over (partition by region order by revenu desc) as highest_revenu
from store;

select products,quatity,revenu,
row_number() over (partition by region order by revenu desc) as highest_revenu
from store;



select region, products,revenu
from store
where Quatity < (selECt AVG(quatity) from store)
and revenu = (select max(revenu) from store);


select max(revenu) from store;

