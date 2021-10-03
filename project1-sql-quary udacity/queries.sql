--frist question (What is the order of the categories in terms of rental ?)

select ca.name,count(r.rental_id)
from category ca
join film_category fc
on ca.category_id=fc.category_id
join film f
on f.film_id=fc.film_id
join inventory
on f.film_id=inventory.film_id
join rental r
on r.inventory_id=inventory.inventory_id
group by 1
order by 2 desc
---------------------------------------------------------------------------------------------------
--second question (What is ordering top 3 category in rental dvd in top 3 country?)

--find top 3 countrywith count_rental_id
with t1 as (select country.country as country ,
			       country.country_id as country_id,
			       count(rental.rental_id)
            from country
            join city
            on country.country_id=city.country_id
            join address
            on address.city_id=city.city_id
            join customer
            on customer.address_id=address.address_id
            join rental
            on customer.customer_id=rental.customer_id
            join inventory
            on rental.inventory_id=inventory.inventory_id
            join film f
            on f.film_id=inventory.film_id
            join film_category
            on film_category.film_id=f.film_id
            join category
            on category.category_id=film_category.category_id
            group by 1,2
            order by 3 desc
            limit 3),
--in_each country find number_rental_id in_each category
 t2 as ( select t1.country as country
		,category.name as category_name,
		count(rental.rental_id)  as count_id
		   from t1
		   join city
            on t1.country_id=city.country_id
            join address
            on address.city_id=city.city_id
            join customer
            on customer.address_id=address.address_id
            join rental
            on customer.customer_id=rental.customer_id
            join inventory
            on rental.inventory_id=inventory.inventory_id
            join film
            on film.film_id=inventory.film_id
            join film_category
            on film_category.film_id=film.film_id
            join category
            on category.category_id=film_category.category_id
		    where category.name in ('Sports','Animation','Action')
            group by 1,2
            order by 3 desc )
select t2.country ,t2.category_name,t2.count_id
from t2
--------------------------------------------------------------------------------------------------------------------
--three question (What is the most 10 actors have large payment)
select r.actor_name,f.rating,sum(pa.amount)
from film f
join inventory
using(film_id)
join rental e
using (inventory_id)
join payment pa
on e.rental_id=pa.rental_id
join(
 select ac.first_name||' '||ac.last_name as actor_name,film_act.film_id as fi
	from actor ac
	join film_actor film_act
	using (actor_id)
) as r
on f.film_id=r.fi
group by 1,2
order by 3 desc
limit 10
-----------------------------------------------------------------------------------------------

--fourth question  (Number_of movies in_each category based_on duration quartile?)
WITH t1 AS (
		SELECT film.title as film_title,
	           category.name AS category_name,
			   NTILE(3) OVER (ORDER BY film.rental_duration) AS standard_quartile
		FROM film
		JOIN film_category
		USING (film_id)
		JOIN category
		USING (category_id)
)
SELECT DISTINCT *
FROM (
SELECT category_name,
	   standard_quartile,
	   COUNT(film_title)
	   OVER(PARTITION BY standard_quartile ORDER BY category_name) AS count
FROM t1
WHERE category_name
IN ('Animation', 'Children', 'Sport', 'Comedy', 'Music')
ORDER BY 1) sub;
