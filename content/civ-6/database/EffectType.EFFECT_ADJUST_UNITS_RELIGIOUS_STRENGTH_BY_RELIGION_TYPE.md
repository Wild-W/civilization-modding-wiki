---
tags:
- EffectType
title: EFFECT_ADJUST_UNITS_RELIGIOUS_STRENGTH_BY_RELIGION_TYPE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNITS_RELIGIOUS_STRENGTH_BY_RELIGION_TYPE
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="WC_RES_RELIGIOUS_UNITS_STRENGTH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"WC_RES_RELIGIOUS_UNITS_STRENGTH",
		"MODIFIER_MAJOR_PLAYERS_ADJUST_UNITS_RELIGIOUS_STRENGTH_BY_RELIGION_TYPE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"WC_RES_RELIGIOUS_UNITS_STRENGTH",
		"Amount",
		10
	);
	
```

