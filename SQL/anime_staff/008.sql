insert into fetch_anime_staff (id,url,mal_id,status,"data",created_at,updated_at,processed) values

ON CONFLICT (id) DO UPDATE  SET url = EXCLUDED.url, status = EXCLUDED.status, "data" = EXCLUDED."data", updated_at = EXCLUDED.updated_at, processed = EXCLUDED.processed;
--select count (id) from fetch_anime_staff;