-- Lista lokacija za novu sadnju  ***  def lil():
SELECT lokacija.id, lokacija.oznaka, lokacija.status, status_lok.opis, sorta.naziv, cokot.poreklo, godinasadnje FROM cokot \
JOIN lokacija \
	ON lokacija.id = cokot.lokacija_id \
JOIN sorta\
	ON sorta.id = cokot.sorta_id \
JOIN status_lok \
	ON lokacija.status = status_lok.status \
WHERE lokacija.status NOT LIKE 'F' AND lokacija.status NOT LIKE 'K' \
ORDER BY  lokacija.id;
   
   
-- čokoti po lokaciji *** def lic(): 
SELECT lokacija.id, lokacija.oznaka, sorta.naziv, epoha.period, lokacija.status, cokot.poreklo, godinasadnje FROM cokot \
JOIN lokacija \
	ON lokacija.id = cokot.lokacija_id \
JOIN sorta\
	ON sorta.id = cokot.sorta_id \
JOIN epoha \
	ON epoha.id = sorta.epoha_id \
WHERE lokacija.status NOT LIKE 'F' \
ORDER BY  lokacija.id;
   r
      
-- lista sorti  *** def lis():
SELECT  sorta.id, sorta.naziv, COUNT(sorta.id) AS cokota FROM cokot \
JOIN lokacija \
	ON lokacija.id = cokot.lokacija_id \
JOIN sorta\
	ON sorta.id = cokot.sorta_id \
WHERE lokacija.status NOT LIKE 'F' \
GROUP BY sorta.id \
ORDER BY  sorta.id;


-- berba sorta, godina, datum, mošt, šećer
SELECT  sorta.naziv, godina.godina, datum_berbe, most, secer  FROM berba
JOIN godina
	ON godina.id = berba.godina_id
JOIN sorta\
	ON sorta.id = berba.sorta_id 
ORDER BY  sorta.id;

-- berba  datum, mošt, šećer
SELECT  godina.godina, datum_berbe, sorta.naziv,  most, secer  FROM berba
JOIN godina
	ON godina.id = berba.godina_id
JOIN sorta\
	ON sorta.id = berba.sorta_id 
ORDER BY  godina.id;


-- Italijanski rizling
SELECT  godina.godina, datum_berbe, ubrano_kg, secer, berba.komentar, most_lit, sira_lit, vina_lit, vina_kom FROM berba
JOIN godina
	ON godina.id = berba.godina_id
JOIN sorta
	ON sorta.id = berba.sorta_id
WHERE sorta.id LIKE 1 
ORDER BY  godina.id;