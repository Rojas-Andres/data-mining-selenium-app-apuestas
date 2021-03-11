create or replace function public.valida_tmp_carga()
returns boolean
language plpgsql
as $function$
declare 

valida integer;
registro record;


cursor_datos cursor is
select distinct 
equipo1 as equipo
from temporal.tmp_carga
union
select distinct 
equipo2 as equipo
from temporal.tmp_carga;

begin 
	
	select count(*) into valida
	from public.equipos;	
	
	for registro in cursor_datos loop
		
		valida = valida+1;
		
		insert into public.equipos (id_equipo ,nom_equipo )
		values
		(valida,registro.equipo) on conflict do nothing ;
	
	end loop;

	
	insert into public.partidos
	select
	b.id_equipo ,
	valor_eq1 ,
	valor_empate ,
	c.id_equipo ,
	valor_eq2 ,
	cast('2021'||'-'||cod_mes||'-'||split_part( a.dia_partido ,' ',1) as date),
	hora_partido
	from
		temporal.tmp_carga a,
		public.equipos b,
		public.equipos c,
		public.meses d
	where
		a.equipo1 = b.nom_equipo
		and a.equipo2 = c.nom_equipo
		and split_part( a.dia_partido ,' ',2)=d.nom_mes_abr on conflict do nothing ;
		
	return true;
end
$function$
;