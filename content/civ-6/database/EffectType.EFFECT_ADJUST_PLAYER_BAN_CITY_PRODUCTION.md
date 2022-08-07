---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_BAN_CITY_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_BAN_CITY_PRODUCTION
>
> * Class: `PLAYERS`
> * Parameters:
>	* BanDistrictBuildings `Boolean`

## Samples
```SQL {title="BAN_DISTRICT_BUILDING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"BAN_DISTRICT_BUILDING",
		"MODIFIER_MAJOR_PLAYERS_ADJUST_BANNED_CITY_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BAN_DISTRICT_BUILDING",
		"BanDistrictBuildings",
		1
	);
	
```

