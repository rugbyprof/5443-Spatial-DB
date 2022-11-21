
CREATE TABLE public.gun (
    name text NOT NULL,
    info text,
    mm numeric,
    ammocat text,
    ammotype text,
    propellantkg numeric,
    rof numeric,
    turnrate numeric
);



INSERT INTO public.gun (name, info, mm, ammocat, ammotype, propellantkg, rof, turnrate) VALUES ('Mark17', '25mm Chain gun', 25, 'cartridge', 'APEX', 0, 250, 360);
INSERT INTO public.gun (name, info, mm, ammocat, ammotype, propellantkg, rof, turnrate) VALUES ('Mark15', '35 mm gatlin gun. ', 35, 'cartridge', 'SAPHEI/SD', 0, 200, 360);
INSERT INTO public.gun (name, info, mm, ammocat, ammotype, propellantkg, rof, turnrate) VALUES ('Mark13', '57 mm gatlin gun. ', 57, 'cartridge', 'L/70 HE', 0, 150, 360);
INSERT INTO public.gun (name, info, mm, ammocat, ammotype, propellantkg, rof, turnrate) VALUES ('Mark11', '120 mm deck mounted gun. Each Mark11 has 2 barrels that can shoot simultaneuously.', 120, 'cartridge', '120 IM HE', 0, 2, 360);
INSERT INTO public.gun (name, info, mm, ammocat, ammotype, propellantkg, rof, turnrate) VALUES ('Mark8', '400 mm deck mounted gun. Each Mark7 has 3 barrels that can shoot simultaneuously.', 400, 'projectile', 'MK13', 120, 3, 90);
INSERT INTO public.gun (name, info, mm, ammocat, ammotype, propellantkg, rof, turnrate) VALUES ('Mark7', '450 mm deck mounted gun. Each Mark7 has 3 barrels that can shoot simultaneuously.', 450, 'projectile', 'MK3', 120, 3, 90);
INSERT INTO public.gun (name, info, mm, ammocat, ammotype, propellantkg, rof, turnrate) VALUES ('Mark5', '475 mm deck mounted gun. Each Mark5 has 3 barrels that can shoot simultaneuously.', 475, 'projectile', 'MK1', 120, 3, 90);

