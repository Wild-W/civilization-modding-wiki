---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_SETTLER_CONSUME_POP
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_SETTLER_CONSUME_POP
>
> * Class: `CITIES`
> * Parameters:
>	* Enabled `Boolean`

## Samples
```SQL {title="EXPEDITION_ADJUST_SETTLERS_CONSUME_POPULATION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"EXPEDITION_ADJUST_SETTLERS_CONSUME_POPULATION",
		"MODIFIER_CITY_ADJUST_SETTLER_CONSUME_POPULATION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"EXPEDITION_ADJUST_SETTLERS_CONSUME_POPULATION",
		"Enabled",
		0
	);
	
```

