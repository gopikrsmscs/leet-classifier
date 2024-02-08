# Write your MySQL query statement below
# lct: sql,join;
select p.firstName , p.lastName , a.city ,a.state from Person as p
left join Address as a
ON p.personId = a.personId;
