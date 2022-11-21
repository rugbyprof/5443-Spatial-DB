

CREATE TABLE public.ship (
    ship_id numeric NOT NULL,
    category text,
    shipclass text,
    displacement numeric,
    length numeric,
    width numeric,
    torpedolaunchers json,
    armament json,
    armor json,
    speed numeric,
    turn_radius numeric
);



INSERT INTO public.ship (ship_id, category, shipclass, displacement, length, width, torpedolaunchers, armament, armor, speed, turn_radius) VALUES (0, 'Battle Ship', 'Beto class', 35000, 180, 31, 'null', '[{"type": "Mark8", "pos": 20}, {"type": "Mark8", "pos": 70}, {"type": "Mark8", "pos": 160}]', '{"hull": 305, "deck": 178}', 28, 25);
INSERT INTO public.ship (ship_id, category, shipclass, displacement, length, width, torpedolaunchers, armament, armor, speed, turn_radius) VALUES (1, 'Battle Ship', 'DIvoire class', 38000, 210, 36, 'null', '[{"type": "Mark7", "pos": 40}, {"type": "Mark8", "pos": 70}, {"type": "Mark8", "pos": 180}]', '{"hull": 305, "deck": 191}', 27, 25);
INSERT INTO public.ship (ship_id, category, shipclass, displacement, length, width, torpedolaunchers, armament, armor, speed, turn_radius) VALUES (2, 'Battle Ship', 'Kılıç class', 48500, 240, 41, 'null', '[{"type": "Mark7", "pos": 60}, {"type": "Mark8", "pos": 120}, {"type": "Mark8", "pos": 180}]', '{"hull": 305, "deck": 203}', 33, 25);
INSERT INTO public.ship (ship_id, category, shipclass, displacement, length, width, torpedolaunchers, armament, armor, speed, turn_radius) VALUES (3, 'Battle Ship', 'Vikrant class', 65000, 270, 46, 'null', '[{"type": "Mark7", "pos": 100}, {"type": "Mark7", "pos": 400}, {"type": "Mark7", "pos": 800}]', '{"hull": 406, "deck": 208}', 28, 25);
INSERT INTO public.ship (ship_id, category, shipclass, displacement, length, width, torpedolaunchers, armament, armor, speed, turn_radius) VALUES (4, 'Battle Ship', 'Yamato class', 71659, 263, 45, 'null', '[{"type": "Mark5", "pos": 10}, {"type": "Mark5", "pos": 70}, {"type": "Mark5", "pos": 130}, {"type": "Mark5", "pos": 190}, {"type": "Mark5", "pos": 250}]', '{"hull": 410, "deck": 226}', 27, 25);
INSERT INTO public.ship (ship_id, category, shipclass, displacement, length, width, torpedolaunchers, armament, armor, speed, turn_radius) VALUES (5, 'Destroyer', 'Z5 class', 2500, 150, 25, 'null', '[{"type": "Mark8", "pos": 20}, {"type": "Mark11", "pos": 50}, {"type": "Mark11", "pos": 80}, {"type": "Mark8", "pos": 1200}]', '{"hull": 20, "deck": 15}', 35, 30);
INSERT INTO public.ship (ship_id, category, shipclass, displacement, length, width, torpedolaunchers, armament, armor, speed, turn_radius) VALUES (6, 'Destroyer', 'Fletcher class', 2325, 115, 20, 'null', '[{"type": "Mark8", "pos": 10}, {"type": "Mark8", "pos": 30}, {"type": "Mark13", "pos": 60}, {"type": "Mark11", "pos": 90}]', '{"hull": 19, "deck": 14}', 35, 30);
INSERT INTO public.ship (ship_id, category, shipclass, displacement, length, width, torpedolaunchers, armament, armor, speed, turn_radius) VALUES (7, 'Destroyer', 'Benson class', 2000, 120, 19, '{"bow": [{"side": "port", "facing": "ahead"}, {"side": "starboard", "facing": "ahead"}], "stern": [{"side": "port", "facing": "astern"}, {"side": "starboard", "facing": "astern"}]}', '[{"type": "Mark8", "pos": 10}, {"type": "Mark13", "pos": 15}, {"type": "Mark11", "pos": 55}, {"type": "Mark11", "pos": 90}, {"type": "Mark8", "pos": 95}]', '{"hull": 18, "deck": 13}', 38, 30);
INSERT INTO public.ship (ship_id, category, shipclass, displacement, length, width, torpedolaunchers, armament, armor, speed, turn_radius) VALUES (8, 'PT Boat', 'Dragon Lady', 55, 24, 7, '{"bow": [{"side": "port", "facing": "ahead"}, {"side": "starboard", "facing": "ahead"}], "stern": [{"side": "port", "facing": "astern"}, {"side": "starboard", "facing": "astern"}]}', '[{"type": "Mark17", "pos": 3}, {"type": "Mark15", "pos": 10}, {"type": "Mark15", "pos": 13}, {"type": "Mark13", "pos": 17}, {"type": "Mark13", "pos": 21}]', '{"hull": 18, "deck": 13}', 74, 45);
INSERT INTO public.ship (ship_id, category, shipclass, displacement, length, width, torpedolaunchers, armament, armor, speed, turn_radius) VALUES (9, 'PT Boat', 'Goddess of War', 50, 24, 7, '{"bow": [{"side": "port", "facing": "ahead"}, {"side": "starboard", "facing": "ahead"}], "stern": [{"side": "port", "facing": "astern"}, {"side": "starboard", "facing": "astern"}]}', '[{"type": "Mark15", "pos": 10}, {"type": "Mark13", "pos": 30}, {"type": "Mark13", "pos": 40}, {"type": "Mark11", "pos": 50}, {"type": "Mark11", "pos": 70}]', '{"hull": 18, "deck": 13}', 80, 45);

