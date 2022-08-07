---
tags:
- EffectType
title: EFFECT_ADJUST_POPULATION_AFTER_CONQUEST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_POPULATION_AFTER_CONQUEST
>
> * Class: `CITIES`
> * Parameters:
>	* Percent `Integer`

## Samples
```SQL {title="TRAIT_CAPTURED_NO_POPULATION_LOSS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_CAPTURED_NO_POPULATION_LOSS",
		"MODIFIER_PLAYER_ADJUST_POPULATION_AFTER_CONQUEST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_CAPTURED_NO_POPULATION_LOSS",
		"Percent",
		100
	);
	
```

