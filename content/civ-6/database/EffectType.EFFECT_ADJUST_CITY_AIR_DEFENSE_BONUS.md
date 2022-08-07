---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_AIR_DEFENSE_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_AIR_DEFENSE_BONUS
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="AIR_DEFENSE_INITIATIVE_ANTI_AIR_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"AIR_DEFENSE_INITIATIVE_ANTI_AIR_BONUS",
		"MODIFIER_CITY_ADJUST_AIR_DEFENSE_BONUS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AIR_DEFENSE_INITIATIVE_ANTI_AIR_BONUS",
		"Amount",
		25
	);
	
```

