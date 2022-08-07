---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_TOURISM_BOMB_NATIONAL_PARK
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_TOURISM_BOMB_NATIONAL_PARK
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="ROCKBAND_MUSIC_FESTIVAL_TOURISM_BOMB"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ROCKBAND_MUSIC_FESTIVAL_TOURISM_BOMB",
		"MODIFIER_PLAYER_UNIT_ADJUST_TOURISM_BOMB_NATIONAL_PARK"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ROCKBAND_MUSIC_FESTIVAL_TOURISM_BOMB",
		"Amount",
		1000
	);
	
```

