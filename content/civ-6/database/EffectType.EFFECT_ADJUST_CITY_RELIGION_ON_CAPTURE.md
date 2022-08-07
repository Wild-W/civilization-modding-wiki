---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_RELIGION_ON_CAPTURE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_RELIGION_ON_CAPTURE
>
> * Class: `CITIES`
> * Parameters:
>	* Enable `Boolean`

## Samples
```SQL {title="CONQUISTADOR_CITY_RELIGION_COMBAT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CONQUISTADOR_CITY_RELIGION_COMBAT",
		"MODIFIER_PLAYER_UNIT_ADJUST_CITY_ON_CAPTURE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CONQUISTADOR_CITY_RELIGION_COMBAT",
		"Enable",
		1
	);
	
```

