---
tags:
- EffectType
title: EFFECT_ADJUST_MODIFIED_FREE_POWER_IN_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_MODIFIED_FREE_POWER_IN_CITY
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`

## Samples
```SQL {title="BIOSPHERE_MODIFIED_FREE_POWER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"BIOSPHERE_MODIFIED_FREE_POWER",
		"MODIFIER_PLAYER_CITIES_ADJUST_MODIFIED_FREE_POWER_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BIOSPHERE_MODIFIED_FREE_POWER",
		"Amount",
		200
	);
	
```

