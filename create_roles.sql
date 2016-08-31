insert into pickem_role (name, description, can_manage_user, can_manage_league, can_manage_game, can_manage_picks)
values('Administrator', 'Full control', true, true, true, true);

insert into pickem_role (name, description, can_manage_user, can_manage_league, can_manage_game, can_manage_picks)
values('User', 'Default access', false, false, false, false);
