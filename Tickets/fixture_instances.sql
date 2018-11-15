SELECT
l.fcid
,l.id
,l.fcid
,l.site_name
,l.sales_designation
,l.language_designation
,ft.fixture_code
,ft.name AS Fixture_type_name
,z.name AS zone
,sz.name AS subzone
,fi.fixture_instance_priority
,fi.within_10_feet
,ft.side_number
FROM public.fixture_instances fi
LEFT JOIN locations l ON l.id = fi.location_id
LEFT JOIN fixture_types ft ON ft.id = fi.fixture_type_id
LEFT JOIN zones z ON z.id = fi.zone_id
LEFT JOIN subzones sz ON sz.id = fi.subzone_id
WHERE ft.side_number = 1
      AND l.bc_status = 'O'
  
