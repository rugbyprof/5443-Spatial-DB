
CREATE TABLE public.torpedo (
    name text,
    guidance text,
    diameter numeric,
    speed numeric,
    kg numeric,
    warheadsize numeric,
    range numeric
);


INSERT INTO public.torpedo (name, guidance, diameter, speed, kg, warheadsize, range) VALUES ('MK42', '0', 570, 102, 1814, 363, 25000);
INSERT INTO public.torpedo (name, guidance, diameter, speed, kg, warheadsize, range) VALUES ('MK39', 'wire guided', 533, 40, 1000, 175, 13000);
INSERT INTO public.torpedo (name, guidance, diameter, speed, kg, warheadsize, range) VALUES ('MK35', 'accoustic', 533, 60, 1300, 150, 15000);
INSERT INTO public.torpedo (name, guidance, diameter, speed, kg, warheadsize, range) VALUES ('MK31', 'accoustic', 570, 50, 1000, 150, 15000);

